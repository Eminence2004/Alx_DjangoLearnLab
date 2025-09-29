# api/urls.py

from django.urls import path, include
# advanced_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # <-- required
]

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

