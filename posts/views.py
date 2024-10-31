from django.shortcuts import render
from .models import Publication
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class PostListView(ListView):
    model = Publication
    template_name = "post_list.html"

class PostCreateView(CreateView):
    model = Publication
    template_name = "post_new.html"
    fields =["title", "author", "text"] #todos los atributos a incluir en la vista

class PostDetailView(DetailView):
    model = Publication
    template_name = "post_detail.html"

class PostUpdateView(UpdateView):
    model = Publication
    template_name = "post_edit.html"
    fields = ["title", "text"]

class PostDeleteView(DeleteView):
    model = Publication
    template_name = "delete.html"
    success_url = reverse_lazy("post_list")
