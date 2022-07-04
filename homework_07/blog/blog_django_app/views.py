from django.http import HttpRequest
from django.shortcuts import render

from .models import User, Post


def users(request: HttpRequest):
    users = User.objects.all()
    context = {
        "users": users,
    }
    return render(request, 'blog/users.html', context=context)


def posts(request: HttpRequest):
    posts = Post.objects.select_related("user").all()
    context = {
        "posts": posts,
    }
    return render(request, 'blog/posts.html', context=context)