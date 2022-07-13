from django.test import TestCase
from django.urls import reverse

from blog_authorization.models import UserModel
from blog_django_app.models import Post


class PostCreationTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        password = "dogpasswd"
        cls.user = UserModel.objects.create_user(username="dog", password=password)
        cls.password = password
        cls.post_data = {"title": "ttl", "body": ""}

    def test_post_creation_access(self):
        response = self.client.get(
            reverse('blog_django_app:post_creation')
        )
        self.assertEqual(302, response.status_code)
        self.assertURLEqual(response.url, reverse('login') + '?next=/post-creation/')

        self.client.login(username=self.user.username, password=self.password)
        response = self.client.get(reverse('blog_django_app:post_creation'))
        self.assertEqual(200, response.status_code)

    def test_post_creation(self):
        self.client.login(username=self.user.username, password=self.password)
        response = self.client.post(
            reverse('blog_django_app:post_creation'),
            data=self.post_data
        )

        self.assertEqual(response.status_code, 302)

        post = Post.objects.get(title=self.post_data["title"])
        self.assertURLEqual(
            response.url,
            reverse('blog_django_app:post_details', kwargs={"pk": post.pk})
        )