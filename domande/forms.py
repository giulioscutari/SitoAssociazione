from django.db import models
from django.forms import ModelForm, forms
from .models import Domanda


class FormDomanda(ModelForm):

    class Meta:
        model = Domanda
        fields = ['domanda', 'prof', 'materia', 'gruppo', 'anno', 'username']