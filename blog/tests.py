from django.test import TestCase

from django.contrib.auth import get_user_model

# Create your tests here.

from .models import Post


class BlogTests(TestCase):
    """
    This is to test the blog application
    """

    @classmethod
    def setUpTestData(cls):
        """
        This sets up the custrm user for testing and also a new test db
        which gets deleted afterwards.
        """
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )

        cls.post = Post.objects.create(
            title="A good title", body="nice content", author=cls.user
        )

    def test_post_model(self):
        """
        This test if the contents are equal in short terms
        """
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "nice content")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "A good title")
        self.assertEqual(self.post.get_absolute_url(), "/post/1")