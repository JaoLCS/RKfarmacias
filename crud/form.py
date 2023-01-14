from .models import *
from django.forms import ModelForm
from django import forms

class remediosForm(ModelForm):
    class Meta:
        model = remedios
        fields = ["rem_remedio","rem_preco","rem_quantidade","rem_embalagem"]