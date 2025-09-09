from django.urls import path
from . import views
from .views import LibraryDetailView, list_books

urlpatterns = [
    # Book listing (previous task)
    path("books/", list_books, name="list_books"),

    # Function-based library detail
    path("library/<int:pk>/", views.library_detail_view, name="library_detail"),

    # Class-based library detail
    path("library/class/<int:pk>/", LibraryDetailView.as_view(), name="library_detail_class"),
]
