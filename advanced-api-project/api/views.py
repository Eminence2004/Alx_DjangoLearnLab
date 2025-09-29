# advanced-api-project/api/views.py
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# List all books (anyone can view)
class ListView(generics.ListAPIView):
    """
    Returns a list of all books.
    Accessible to anyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Retrieve a single book’s detail (only authenticated)
class DetailView(generics.RetrieveAPIView):
    """
    Returns the details of a single book.
    Accessible to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
