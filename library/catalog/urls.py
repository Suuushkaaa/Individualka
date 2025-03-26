from django.urls import path, re_path, include
from .import views
from rest_framework.routers import DefaultRouter
from rest_framework import routers, serializers, viewsets
from .models import Book
from django.contrib.auth.models import User
# from .views import BookViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from .views import api_root, SnippetViewSet, UserViewSet, AuthorView, SingleAuthorView, UserSerializer, AuthorViewSet, AuthorViewS
#ssssss
# from .views import api_root, SnippetViewSet, UserViewSet, AuthorView, AuthorViewSet, UserSerializer
from rest_framework.routers import Route, DynamicRoute, SimpleRouter


#НАДАfvfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
snippet_list = SnippetViewSet.as_view({
'get': 'list',
'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
'get': 'retrieve',
'put': 'update',
'patch': 'partial_update',
'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
'get': 'list'
})
user_detail = UserViewSet.as_view({
'get': 'retrieve'
})




# class CustomReadOnlyRouter(SimpleRouter):
#     routes = [
#     Route(
#     url=r'^{prefix}$',
#     mapping={'get': 'list'},
#     name='{basename}-list',
#     detail=False,
#     initkwargs={'suffix': 'List'}
#     ),
#     Route(
#     url=r'^{prefix}/{lookup}$',
#     mapping={'get': 'retrieve'},
#     name='{basename}-detail',
#     detail=True,
#     initkwargs={'suffix': 'Detail'}
#     ),
#     DynamicRoute(
#     url=r'^{prefix}/{lookup}/{url_path}$',
#     name='{basename}-{url_name}',
#     detail=True,
#     initkwargs={}
#     )
#     ]


# app_name = "bookss"


#РАБОТАЕТ, но 2ой способ лучше(с48стр)
# class UsersSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'is_staff']
# ViewSets define the view behavior.
# class UsersViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
# router = routers.DefaultRouter()
# router.register(r'us', UsersViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors-list'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='authors-detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    re_path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    # path('bb/', BookViewS.as_view()),

    # path('bb/<int:pk>', BookViewS.as_view()),

    path('authorss/', AuthorView.as_view()),
    path('authorss/<int:pk>', SingleAuthorView.as_view()),

    #ssssss
    path('aut/', AuthorViewS.as_view({'get': 'list'})),
    path('aut/<int:pk>', AuthorViewSet.as_view({'get': 'retrieve'})),


    
    path('gena/', views.GenreInfoView.as_view()),
    
    
    
    # path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #psge58 work(json format)
    #page61 with format work
    path('genres/', views.genre_list),
    path('genres/<int:pk>/', views.genre_detail),
    path('pu/', views.publisher_list),
    path('pu/<int:pk>/', views.publisher_detail),

    #page65 work
    #page67. 66 work

    path('languages/', views.LanguageList.as_view()),
    path('languages/<int:pk>/', views.LanguageDetail.as_view()),
    path('pubs/', views.PublisherList.as_view()),
    path('pubs/<int:pk>/', views.PublisherDetail.as_view()),
    # path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    # # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('inst/', views.InstanceList.as_view()),
    path('inst/<int:pk>/', views.InstanceDetail.as_view()),

    #НАДАfvfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    path('api/', api_root),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),

    path('us/',views.UserCountView.as_view() ),

    
    # path('aa/<int:pk>/', views.AuthDetail.as_view(), name='author_detail'),
    # path('m/<int:image_id>/', views.JPEGRenderer, name="image"),
    path('auu/', views.list_users),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

 ]
urlpatterns = format_suffix_patterns(urlpatterns)
# router = CustomReadOnlyRouter()
# router.register('u', UserViewSets)
# urlpatterns = router.urls
#НАДАfvfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='users')

# urlpatterns = [
# path('', include(router.urls)),
# ]
# Routers provide an easy way of automatically determining the URL conf.

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.



