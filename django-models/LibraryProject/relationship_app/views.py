from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Library, Book


# Function-based view (already required)
def library_detail_view(request, pk):
    library = Library.objects.get(pk=pk)
    books = library.book_set.all()
    return render(request, "relationship_app/library_detail.html", {"library": library, "books": books})


# Class-based view (DetailView)
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.book_set.all()
        return context
