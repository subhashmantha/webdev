# posts/urls.py
from django.urls import path
from .views import HomePageView, AboutView, PostDetailView


urlpatterns = [
path("", HomePageView.as_view(), name="posts_home"),
path("about", AboutView.as_view(), name="about"),
path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
]