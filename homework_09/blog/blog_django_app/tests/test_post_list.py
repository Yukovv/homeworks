from django.test import TestCase
from django.urls import reverse

from blog_django_app.models import Post


class PostsTestCase(TestCase):
    fixtures = [
        "posts.fixture.json",
        "users.fixture.json",
    ]

    def test_post_list(self):
        response = self.client.get(
            reverse("blog_django_app:posts")
        )

        self.assertEqual(response.status_code, 200)

        posts_list = Post.objects.order_by("id")
        posts_in_context = response.context["post_list"]
        self.assertEqual(len(posts_list), len(posts_in_context))
        for post1, post2 in zip(posts_list, posts_in_context):
            self.assertEqual(post1.pk, post2.pk)

    def test_post_list_anon_access(self):
        response = self.client.get(
            reverse("blog_django_app:posts")
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["user"].is_anonymous)
