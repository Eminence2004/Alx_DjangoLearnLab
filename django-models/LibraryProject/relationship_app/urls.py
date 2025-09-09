from django.urls import path
from . import views
from .views import LibraryDetailView

urlpatterns = [
      path('library/<int:pk>/', views.library_detail_view, name='library_detail'),

    # Class-based view
    path('library/class/<int:pk>/', LibraryDetailView.as_view(), name='library_detail_class'),
]
