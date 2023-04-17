from django.forms import ModelForm
from .models import User
class UserRegistration(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']