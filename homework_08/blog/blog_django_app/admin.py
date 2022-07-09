from django.contrib import admin

from .models import User, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "user")

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related("user")


admin.site.register(Post, PostAdmin)
