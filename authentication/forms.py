from dataclasses import fields
from socket import fromshare
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms 

class RegisterUserForm(UserCreationForm):
    password1: forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_input'}))
    password2: forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_input'}))

    class Meta:
        model = User
        fields = ['username']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form_input'})
        }