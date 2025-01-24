from django.urls import path, re_path
from .import views
from .views import BookView, SingleBookView

# app_name = "bookss"

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
    path('bookss/', BookView.as_view()),
# #     path('articles/<int:pk>', BookView.as_view()),
    path('bookss/<int:pk>', SingleBookView.as_view()),
 ]