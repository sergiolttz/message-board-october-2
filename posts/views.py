from django.shortcuts import render
from .models import Publication
from django.views.generic import ListView

# Create your views here.
class PostListView(ListView):
    model = Publication
    template_name = "post_list.html"