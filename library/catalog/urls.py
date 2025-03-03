from django.urls import path, re_path, include
from .import views
from rest_framework.routers import DefaultRouter
from rest_framework import routers, serializers, viewsets
from .models import Book
from django.contrib.auth.models import User
# from .views import BookViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from .views import api_root, SnippetViewSet, UserViewSet

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
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'is_staff']
# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)


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
    # path('bookss/', BookView.as_view()),
# #   path('articles/<int:pk>', BookView.as_view()),
    # path('bookss/<int:pk>', SingleBookView.as_view()),
    # path('bookss/', BookViewSet.as_view({'get': 'list'})),
    # path('bookss/<int:pk>', BookViewSet.as_view({'get': 'retrieve'})),

    
    # path('api/boooks/', views.GetBookInfoView.as_view()),
    
    
    
    # path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #psge58 work(json format)
    #page61 with format work
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>/', views.snippet_detail),

    #page65 work
    #page67. 66 work

    # path('snippets/', views.SnippetList.as_view()),
    # path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    # path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    # # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # path('users/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view()),

    #НАДАfvfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
    path('api/', api_root),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

 ]
urlpatterns = format_suffix_patterns(urlpatterns)
# router = CustomReadOnlyRouter()
# router.register('users', UserViewSet)
# urlpatterns = router.urls
#НАДАfvfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

# urlpatterns = [
# path('', include(router.urls)),
# ]
# Routers provide an easy way of automatically determining the URL conf.

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.



