from django.urls import path
from .views import (
                    PostListView,
                    PostCreateView,
                    PostDetailView,
                    PostUpdateView,
                    PostDeleteView,
                )

urlpatterns = [
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("", PostListView.as_view(), name="post_list"),
    path("post/new/", PostCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/edit", PostUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="post_delete"),

]