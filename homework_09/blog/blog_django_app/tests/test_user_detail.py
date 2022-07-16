from django.test import TestCase
from django.urls import reverse

from blog_authorization.models import UserModel
from blog_django_app.models import Post


class UserDetailTest(TestCase):
    fixtures = [
        "posts.fixture.json",
        "users.fixture.json",
    ]

    def test_user_posts(self):
        users = UserModel.objects.all()

        for user in users:
            response = self.client.get(
                reverse('blog_django_app:user_details', kwargs={"pk": user.pk})
            )

            user_posts = Post.objects.filter(user=user)
            user_posts_in_context = response.context["user_posts"]

            self.assertEqual(len(user_posts), len(user_posts_in_context))
