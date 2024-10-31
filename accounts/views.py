from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class SignUpView(CreateView):
    template_name = "registration/signup.html"
    succes_url = reverse_lazy("login")
    form_class = UserCreationForm

