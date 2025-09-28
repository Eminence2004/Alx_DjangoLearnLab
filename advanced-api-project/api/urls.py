# api/urls.py
from django.urls import path
from .views import (
    BookListCreateView, 
    BookUpdateView, 
    BookDeleteView
)

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]
