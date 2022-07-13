from django.test import TestCase
from django.urls import reverse

from blog_django_app.models import User


class UsersTestCase(TestCase):
    fixtures = [
        "users.fixture.json",
    ]

    def test_users_list(self):
        response = self.client.get(
            reverse("blog_django_app:users")
        )

        self.assertEqual(response.status_code, 200)

        users_list = User.objects.filter(is_staff=False).order_by("id")
        users_in_context = response.context["user_list"]
        self.assertEqual(len(users_list), len(users_in_context))
        for user1, user2 in zip(users_list, users_in_context):
            self.assertEqual(user1.pk, user2.pk)

    def test_users_list_anon_access(self):
        response = self.client.get(
            reverse("blog_django_app:users")
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["user"].is_anonymous)
