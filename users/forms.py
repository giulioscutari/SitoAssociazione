from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    nome = forms.CharField()
    cognome = forms.CharField()

    class Meta:
        model = User
        fields = ['nome', 'cognome', 'username', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,
        }
