# advanced-api-project/api/views.py
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# Create a new Book
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # only authenticated users can create
    permission_classes = [permissions.IsAuthenticated]

# Update an existing Book
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # only authenticated users can update
    permission_classes = [permissions.IsAuthenticated]

# Delete a Book
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # only staff/admin can delete
    permission_classes = [permissions.IsAdminUser]
