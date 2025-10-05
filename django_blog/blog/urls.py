from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # You can add more paths here for comments, user registration, etc.
      path('posts/<int:post_id>/comments/new/', views.add_comment, name='add-comment'),
    path('comments/<int:pk>/edit/', views.edit_comment, name='edit-comment'),
    path('comments/<int:pk>/delete/', views.delete_comment, name='delete-comment'),
]
