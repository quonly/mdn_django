from django.urls import path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
  path('',views.index,name='index'),
  path('books/',views.BookListView.as_view(), name='books'),
  path('books/<int:pk>',views.BookDetailView.as_view(), name='book-detail'),
  path('books/love/',views.BookLoveListView.as_view(), name='books-love'),
]