# posts/views.py
from django.views.generic import ListView
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = "posts_home.html"
