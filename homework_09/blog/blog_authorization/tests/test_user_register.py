from django.contrib.auth.forms import UserCreationForm
from django.test import TestCase
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from blog_authorization.models import UserModel


class UserRegisterTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user_data = {
            "username": "dog",
            "password1": "dogpasswd",
            "password2": "dogpasswd",
        }
        cls.user_data_mismatched_passwords = {
            "username": "dog",
            "password1": "dogpasswd",
            "password2": "passwddog",
        }

    def test_user_register_success(self):
        response = self.client.post(
            reverse('register'),
            data=self.user_data,
        )
        self.assertEqual(302, response.status_code)
        self.assertURLEqual(response.url, reverse('blog_django_app:users'))

        user = UserModel.objects.get(username=self.user_data["username"])
        self.assertTrue(user)

    def test_user_register_username_exist_error(self):
        response = self.client.post(
            reverse('register'),
            data=self.user_data,
        )
        self.assertEqual(302, response.status_code)

        response = self.client.post(
            reverse('register'),
            data=self.user_data,
        )
        self.assertEqual(200, response.status_code)

        self.assertFormError(
            response,
            "form",
            "username",
            _("A user with that username already exists."),
        )

    def test_user_register_mismatched_passwords(self):
        response = self.client.post(
            reverse('register'),
            data=self.user_data_mismatched_passwords,
        )
        self.assertEqual(200, response.status_code)

        self.assertFormError(
            response,
            "form",
            "password2",
            UserCreationForm.error_messages["password_mismatch"],
        )