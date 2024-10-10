from django.shortcuts import render
from .models import Publication
from django.views.generic import ListView
from django.views.generic.edit import CreateView

# Create your views here.
class PostListView(ListView):
    model = Publication
    template_name = "post_list.html"

class PostCreateView(CreateView):
    model = Publication
    template_name = "post_new.html"
    fields =["text",] #todos los atributos a incluir en la vista
    