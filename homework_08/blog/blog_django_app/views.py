from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import User, Post


class UserListView(ListView):
    model = User
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

