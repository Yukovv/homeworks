from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import (
    LogoutView as LogoutViewGeneric,
    LoginView as LoginViewGeneric,
)

from .forms import UserCreationForm
from .models import UserModel


class UserCreationView(CreateView):
    model = UserModel
    success_url = reverse_lazy("blog_django_app:users")
    form_class = UserCreationForm
    template_name = "blog_authorization/register.html"


class LoginView(LoginViewGeneric):
    next_page = reverse_lazy("blog_django_app:users")
    template_name = "blog_authorization/login.html"


class LogoutView(LogoutViewGeneric):
    next_page = reverse_lazy("blog_django_app:users")
