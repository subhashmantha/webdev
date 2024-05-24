# posts/urls.py
from django.urls import path
from .views import HomePageView, AboutView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView


urlpatterns = [
path("", HomePageView.as_view(), name="posts_home"),
path("about", AboutView.as_view(), name="about"),
path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
path("post/new/", PostCreateView.as_view(), name="post_new"),
path("post/<int:pk>/edit/", PostUpdateView.as_view(),
name="post_edit"),
path("post/<int:pk>/delete/", PostDeleteView.as_view(),
name="post_delete"), # new
]