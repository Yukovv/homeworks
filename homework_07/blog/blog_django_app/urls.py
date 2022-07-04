from django.urls import path

from .views import users

app_name = "blog_django_app"

urlpatterns = [
    path('users/', users, name="users"),
]