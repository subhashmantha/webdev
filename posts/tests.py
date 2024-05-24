from django.test import TestCase
from .models import Post
from django.urls import reverse # new


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")
    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")

    def test_url_exists_at_correct_location(self): # new
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, 200)
    def test_url_available_by_name(self): # new
        response = self.client.get(reverse("posts_home"))
        self.assertEqual(response.status_code, 200)
    def test_template_name_correct(self): # new
        response = self.client.get(reverse("posts_home"))
        self.assertTemplateUsed(response, "posts_home.html")

    def test_template_content(self): # new
        response = self.client.get(reverse("posts_home"))
        self.assertContains(response, "This is a test!")

    def test_homepage(self):  # new
        response = self.client.get(reverse("posts_home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts_home.html")
        self.assertContains(response, "This is a test!")

