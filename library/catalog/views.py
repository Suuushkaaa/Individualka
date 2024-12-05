from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance
from django.views.generic import ListView, DetailView

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

