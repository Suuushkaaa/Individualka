from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Book, Author, BookInstance, Cart, CartItem, Genre, Language, Publisher
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from rest_framework.views import APIView
from .serializers import BookSerializer, UserSerializer, AuthorSerializer, GenreSerializer, LanguageSerializer, PublisherSerializer, BookInstanceSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import  ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework import mixins, generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.decorators import action
from rest_framework.renderers import JSONRenderer
from rest_framework.renderers import TemplateHTMLRenderer, StaticHTMLRenderer

# Create your views here.

# def index(request):
#     return HttpResponse("Главная страница сайта Книжный червь!")

def index(request):
    text_head = 'На нашем сайте вы можете получить книги в электронном виде'
    # Данные о книгах и их количестве
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    # Данные об экземплярах книг в БД
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'На складе')
    num_instances_available = BookInstance.objects.filter(
    status__exact=2).count()
    # Данные об авторах книг
    authors = Author.objects
    num_authors = Author.objects.count()
    # Словарь для передачи данных в шаблон index.html
    context = {'text_head': text_head,
    'books': books, 'num_books': num_books,
    'num_instances': num_instances,
    'num_instances_available': num_instances_available,
    'authors': authors, 'num_authors': num_authors}
    # передача словаря context с данными в шаблон
    return render(request, 'catalog/index.html', context)

class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    paginate_by = 3

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'

class AuthorListView(ListView):
    model = Author
    paginate_by = 4

class AuthorDetailView(DetailView):
    model = Author

class LoanedBooksByUserListView(LoginRequiredMixin, ListView):

    model = BookInstance
    template_name = 'catalog/borrowed.html'
    paginate_by = 10
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).order_by('due_back')


def about(request):
    text_head = 'Сведения о компании'
    name = 'ООО "Интеллектуальные информационные системы"'
    rab1 = 'Разработка приложений на основе' \
    ' систем искусственного интеллекта'
    rab2 = 'Распознавание объектов дорожной инфраструктуры'
    rab3 = 'Создание графических АРТ-объектов на основе' \
    ' систем искусственного интеллекта'
    rab4 = 'Создание цифровых интерактивных книг, учебных пособий' \
    ' автоматизированных обучающих систем'
    context = {'text_head': text_head, 'name': name,
    'rab1': rab1, 'rab2': rab2,
    'rab3': rab3, 'rab4': rab4}
    # передача словаря context с данными в шаблон
    return render(request, 'catalog/about.html', context)

def contact(request):
    text_head = 'Контакты'
    name = 'ООО "Интеллектуальные информационные системы"'
    address = 'Москва, ул. Планерная, д.20, к.1'
    tel = '495-345-45-45'
    email = 'iis_info@mail.ru'
    # Словарь для передачи данных в шаблон index.html
    context = {'text_head': text_head,
    'name': name, 'address': address,
    'tel': tel,
    'email': email}
    # передача словаря context с данными в шаблон
    return render(request, 'catalog/contact.html', context)

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def add_to_cart(request, product_id):
    product = get_object_or_404(Book, id=product_id)

    if request.user.is_authenticated:
        try:
            cart, created = BookInstance.objects.get_or_create(borrower=request.user)
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

            cart_item.save()
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    else:
        cart = request.session.get('cart', [])
        if product_id not in cart:
            cart.append(product_id)
        request.session['cart'] = cart
    return JsonResponse({'success': True, 'message': 'Товар успешно добавлен в корзину!'})

#не разобрались
# class BookViewS(APIView):
#     def get(self, request):
#         books=Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response({"books": serializer.data})
#     def post(self, request):
#         book= request.data.get('books')
#         # Create an article from the above data
#         serializer = BookSerializer(data=book)
#         if serializer.is_valid(raise_exception=True):
#             book_saved = serializer.save()
#         return Response({"success": "Book '{}' created successfully".format(book_saved.title)})
#     def put(self, request, pk):
#         saved_book = get_object_or_404(Book.objects.all(), pk=pk)
#         data = request.data.get('books')
#         serializer = BookSerializer(instance=saved_book, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             book_saved = serializer.save()
#         return Response({ "success": "Article '{}' updated successfully".format(book_saved.title)})
#     def delete(self, request, pk):
#         # Get object with this pk
#         article = get_object_or_404(Book.objects.all(), pk=pk)
#         article.delete()
#         return Response({
#         "message": "Article with id `{}` has been deleted.".format(pk)}, status=204)


# Django API part2

class AuthorView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    def perform_create(self, serializer):
        # author = get_object_or_404(Author, id=self.request.data.get('author'))
        return serializer.save()
class SingleAuthorView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer




#ssssss
class AuthorViewS(viewsets.ViewSet):
    def list(self, request):
        queryset = Author.objects.all()
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        queryset = Author.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = AuthorSerializer(user)
        return Response(serializer.data)

class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()



class GenreInfoView(APIView):
    def get(self, request):
        queryset = Genre.objects.all()
        serializer_for_queryset = GenreSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)



#json format
@csrf_exempt
def publisher_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Publisher.objects.all()
        serializer = PublisherSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PublisherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def publisher_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Publisher.objects.get(pk=pk)
    except Publisher.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = PublisherSerializer(snippet)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PublisherSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


#РАБОТАЕТ
@api_view(['GET', 'POST'])
def genre_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Genre.objects.all()
        serializer = GenreSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def genre_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = GenreSerializer(snippet)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = GenreSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#РФБОТАЕТ
class LanguageList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Language.objects.all()
        serializer = LanguageSerializer(snippets, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = LanguageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LanguageDetail(APIView):
    """
    65
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Language.objects.get(pk=pk)
        except Language.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = LanguageSerializer(snippet)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = LanguageSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#РФБОТАЕТ
class PublisherList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class PublisherDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


#РАБОТАЕТ
class InstanceList(generics.ListCreateAPIView):
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)
    permission_classes = [IsOwnerOrReadOnly]
class InstanceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer
    permission_classes = [IsOwnerOrReadOnly]
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsOwnerOrReadOnly]
#     # def perform_create(self, serializer):
#     #     serializer.save(owner=self.request.user)
#     # permission_classes = [IsOwnerOrReadOnly]
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsOwnerOrReadOnly]




#НАДАfvfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
'users': reverse('user-list', request=request, format=format),
'snippets': reverse('snippet-list', request=request, format=format)
})
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
class SnippetViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    Additionally we also provide an extra `highlight` action.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsOwnerOrReadOnly]
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# class UserViewSets(viewsets.ReadOnlyModelViewSet):
#     """
#     A viewset that provides the standard actions
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_field = 'username'
#     @action(detail=True)
#     def group_names(self, request, pk=None):
#         user = self.get_object()
#         groups = user.groups.all()
#         return Response([group.name for group in groups])

class UserCountView(APIView):
    """
    A view that returns the count of active users in JSON.
    """
    renderer_classes = [JSONRenderer]
    def get(self, request, format=None):
        user_count = User.objects.filter(is_active=True).count()
        content = {'user_count': user_count}
        return Response(content)
    

    
# class AuthDetail(generics.RetrieveAPIView):
#     queryset = Author.objects.all()
#     renderer_classes = [TemplateHTMLRenderer]
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return Response({'user': self.object}, template_name='catalog/author_detail.html')


# class JPEGRenderer(renderers.BaseRenderer):
#     media_type = 'images/jpeg'
#     format = 'jpg'
#     charset = None
#     render_style = 'binary'
#     def render(self, data, accepted_media_type=None, renderer_context=None):
#         return data

# @api_view(['GET'])
# @renderer_classes([TemplateHTMLRenderer, JSONRenderer])
# def list_users(request):
#         queryset = User.objects.filter(is_superuser=False)
#         if request.accepted_renderer.format == 'html':
#         # TemplateHTMLRenderer takes a context dict,
#         # and additionally requires a 'template_name'.
#         # It does not require serialization.
#             data = {'users': queryset}
#             return Response(data, template_name='catalog/author_list.html')
#     # JSONRenderer requires serialized data as normal.
#         serializer = UserSerializer(instance=queryset)
#         data = serializer.data
#         return Response(data)


