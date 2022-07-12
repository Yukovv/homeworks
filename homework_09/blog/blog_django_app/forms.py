from django.forms import ModelForm, CharField

from .models import Post


class PostCreationForm(ModelForm):

    class Meta:
        model = Post
        fields = "title", "body", "user"


