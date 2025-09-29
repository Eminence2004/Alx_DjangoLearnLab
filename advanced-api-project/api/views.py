from rest_framework import generics, permissions
from rest_framework import generics, filters as drf_filters
from django_filters import rest_framework as filters
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


# List all books
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # read-only for everyone
     permission_classes = [IsAuthenticatedOrReadOnly]



    # ✅ Filtering, Searching and Ordering:
    filter_backends = [
        filters.DjangoFilterBackend,     # filtering
        drf_filters.SearchFilter,        # searching
        drf_filters.OrderingFilter       # ordering
    ]

    # allow filtering by these fields
    filterset_fields = ['title', 'author', 'publication_year']

    # allow searching text in these fields
    search_fields = ['title', 'author__name']  # if Author has a field name

    # allow ordering by these fields
    ordering_fields = ['title', 'publication_year']



# Retrieve a single book
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Create a new book
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Update an existing book
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Delete a book
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAdminUser]


