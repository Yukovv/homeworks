from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from blog_authorization.models import UserModel


class UserLoginTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        password = "dogpasswd"
        cls.user: User = UserModel.objects.create_user(username="dog", password=password)
        cls.password = password
        cls.incorrect_password = "passwddog"

    def test_user_login(self):
        response = self.client.post(
            reverse('login'),
            data={
                "username": self.user.username,
                "password": self.password,
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertURLEqual(response.url, reverse("blog_django_app:users"))

    def test_user_login_unsuccessful(self):
        response = self.client.post(
            reverse('login'),
            data={
                "username": self.user.username,
                "password": self.incorrect_password,
            }
        )

        self.assertEqual(response.status_code, 200)
