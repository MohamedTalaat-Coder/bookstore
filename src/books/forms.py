from django.forms import ModelForm
from django import forms
from .models import Books
class BooksForm(ModelForm):
    class Meta:
        model = Books
        exclude = ("id","date")
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
        }