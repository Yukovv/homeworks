from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from .forms import PostCreationForm
from .models import User, Post


class UserListView(ListView):
    queryset = User.objects.filter(is_staff=False)
    template_name = "blog/users.html"


class PostListView(ListView):
    queryset = Post.objects.select_related("user")
    template_name = "blog/posts.html"


class PostDetailsView(DetailView):
    queryset = Post.objects.select_related("user")
    template_name = "blog/post_details.html"


class UserDetailsView(DetailView):
    model = User
    template_name = "blog/user_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_posts"] = Post.objects.filter(user=self.object).all()
        return context


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreationForm
    template_name = "blog/post_creation.html"

    def get_success_url(self):
        return reverse("blog_django_app:post_details", kwargs={"pk": self.object.pk})

