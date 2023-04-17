from django.shortcuts import render
from django.views.generic import CreateView
# Create your views here.
from .views import *
from .forms import *

class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistration
    template_name = 'account/registration.html'
