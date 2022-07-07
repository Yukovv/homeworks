from django.urls import path

from .views import (
    # users,
    UserListView,
    # posts,
    PostListView,
    post_details,
    user_details,
)

app_name = "blog_django_app"

urlpatterns = [
    path('users/', UserListView.as_view(), name="users"),
    path('users/<int:pk>/', user_details, name="user_details"),
    path('posts/', PostListView.as_view(), name="posts"),
    path('posts/<int:pk>/', post_details, name="post_details"),
]