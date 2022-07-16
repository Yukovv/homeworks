from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from blog_authorization.models import UserModel


class UserLogoutTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        password = "dogpasswd"
        cls.user: User = UserModel.objects.create_user(username="dog", password=password)
        cls.password = password

    def test_user_logout(self):
        response = self.client.post(
            reverse("login"),
            data={
                "username": self.user.username,
                "password": self.password,
            }
        )

        response = self.client.get(reverse("blog_django_app:users"))
        self.assertFalse(response.context["user"].is_anonymous)

        response = self.client.get(
            reverse("logout")
        )

        self.assertEqual(response.status_code, 302)
        self.assertURLEqual(response.url, reverse("blog_django_app:users"))

        response = self.client.get(reverse("blog_django_app:users"))
        self.assertTrue(response.context["user"].is_anonymous)
