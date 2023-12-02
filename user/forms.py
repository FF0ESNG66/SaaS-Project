from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . import models


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=20)
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))

    class Meta:
        model = models.CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'date_of_birth', 'password1', 'password2']


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = models.CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'date_of_birth', 'password']
    