from django.urls import path
from .views import (
    list_books,
    library_detail_view,
    LibraryDetailView,
    register_view,
    login_view,
    logout_view,
)

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", library_detail_view, name="library_detail_fbv"),
    path("library/class/<int:pk>/", LibraryDetailView.as_view(), name="library_detail_cbv"),

    # Authentication
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
