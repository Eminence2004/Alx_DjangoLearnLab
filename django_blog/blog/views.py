# blog/views.py
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Comment
from .forms import PostForm
from .forms import CommentForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render, redirect


# registration view already:
from .forms import CustomUserCreationForm


# --- List all posts ---
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # templates/blog/post_list.html
    context_object_name = 'posts'
    ordering = ['-created_at']  # newest first (if you have a created_at field)


# --- Show one post ---
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # templates/blog/post_detail.html
    context_object_name = 'post'


# --- Create a new post (must be logged in) ---
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'  # templates/blog/post_form.html

    def form_valid(self, form):
        form.instance.author = self.request.user  # set author automatically
        return super().form_valid(form)


# --- Update an existing post (must be author) ---
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'  # reuse same form template

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# --- Delete a post (must be author) ---
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'  # templates/blog/post_confirm_delete.html
    success_url = reverse_lazy('post-list')  # redirect after delete

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    




# --- Add a comment to a post (must be logged in) ---
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form, 'post': post})


def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.author != request.user:
        return redirect('post-detail', pk=comment.post.pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/comment_form.html', {'form': form})


def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_id = comment.post.pk
    if comment.author == request.user:
        comment.delete()

    return redirect('post-detail', pk=post_id)



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'registration/profile.html', {'form': form})
