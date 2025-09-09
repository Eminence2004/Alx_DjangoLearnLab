from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm

# Create your views here.
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

def form_example_view(request):
    results = None
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['search_query']
            # Safe ORM query, prevents SQL injection
            results = Book.objects.filter(title__icontains=query)
    else:
        form = ExampleForm()

    return render(request, "bookshelf/form_example.html", {"form": form, "results": results})

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    return HttpResponse("Book created (only if you have can_create permission).")

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return HttpResponse(f"Editing book: {book.title} (requires can_edit permission).")

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return HttpResponse(f"Deleting book: {book.title} (requires can_delete permission).")


