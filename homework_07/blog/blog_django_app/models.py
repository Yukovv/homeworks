from django.db import models


class User(models.Model):
    name = models.CharField(max_length=64, unique=True)
    email = models.CharField(null=False, max_length=32, unique=True)
    about = models.TextField(blank=True, null=False, max_length=500)
