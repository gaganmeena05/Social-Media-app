import email
from django import froms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm

class UserRegisterForm(UserCreationForm):
    email = froms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']