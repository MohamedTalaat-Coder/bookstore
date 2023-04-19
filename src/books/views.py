from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Books
from .forms import BooksForm


# Create your views here.

class HomePage(ListView):
    template_name = "base.html"



class CreateBook(CreateView):
    template_name = "base.html"
    model = Books
    form_class = BooksForm
