from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.

class HomePage(ListView):
    template_name = "base.html"
    