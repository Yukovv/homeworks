from django.urls import path

from .views import users, posts, post_details

app_name = "blog_django_app"

urlpatterns = [
    path('users/', users, name="users"),
    path('posts/', posts, name="posts"),
    path('posts/<int:pk>/', post_details, name="post_details"),
]