from django.urls import reverse
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
        
    def test_url_exist_at_correct_location_listview(self):
        """
        docstring
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_url_exist_at_correct_location_detaailview(self):
        """
        docstring
        """
        response = self.client.get('/post/1')
        self.assertEqual(response.status_code, 200)
        
    def test_post_listview(self):
        """
        docstring
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'nice content')
        self.assertTemplateUsed(response, 'home.html')
        
    def test_post_detailview(self):
        """
        docstring
        """
        response = self.client.get(reverse('post_detail',kwargs={'pk':self.post.pk}))
        no_response = self.client.get('/post/100000')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')
        
        