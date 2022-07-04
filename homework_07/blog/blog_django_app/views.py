from django.http import HttpRequest
from django.shortcuts import render

from .models import User


def users(request: HttpRequest):
    users = User.objects.all()
    context = {
        "users": users,
    }
    return render(request, 'blog/users.html', context=context)
