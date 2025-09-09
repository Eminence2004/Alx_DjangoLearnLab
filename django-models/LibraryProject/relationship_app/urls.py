from django.urls import path
from .views import list_books, library_detail_view, LibraryDetailView

urlpatterns = [
    path("books/", list_books, name="list_books"),  # FBV for books
    path("library/<int:pk>/", library_detail_view, name="library_detail_fbv"),  # FBV for library
    path("library/class/<int:pk>/", LibraryDetailView.as_view(), name="library_detail_cbv"),  # CBV for library
]
