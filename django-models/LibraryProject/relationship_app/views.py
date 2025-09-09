from django.shortcuts import render
from .models import Library, Book  # make sure Book is imported

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})




