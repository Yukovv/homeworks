from django.urls import path

from .views import users, posts

app_name = "blog_django_app"

urlpatterns = [
    path('users/', users, name="users"),
    path('posts/', posts, name="posts"),
]