from django.shortcuts import render
from .models import Publication
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

# Create your views here.
class PostListView(ListView):
    model = Publication
    template_name = "post_list.html"

class PostCreateView(CreateView):
    model = Publication
    template_name = "post_new.html"
    fields =["title", "author", "text",] #todos los atributos a incluir en la vista
    
class PostDetailView(DetailView):
    model = Publication
    template_name = "post_detail.html"