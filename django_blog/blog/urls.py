from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView,
    add_comment, edit_comment, delete_comment
)

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # ✅ intuitive comment URLs
    path('posts/<int:post_id>/comments/new/', add_comment, name='comment-create'),
    path('comments/<int:pk>/edit/', edit_comment, name='comment-update'),
    path('comments/<int:pk>/delete/', delete_comment, name='comment-delete'),
]
