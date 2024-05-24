# posts/views.py
from django.views.generic import ListView, TemplateView, DetailView
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = "posts_home.html"
class AboutView(TemplateView):
    template_name = "about.html"

class PostDetailView(DetailView): # new
    model = Post
    template_name = "post_detail.html"