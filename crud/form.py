from .models import *
from django.forms import ModelForm
from django import forms

class remediosForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rem_remedio'].widget.attrs.update({'class': 'form-control ps-0 form-control-line'}) 
        self.fields['rem_preco'].widget.attrs.update({'class': 'form-control ps-0 form-control-line'}) 
        self.fields['rem_quantidade'].widget.attrs.update({'class': 'form-control ps-0 form-control-line'}) 
        self.fields['rem_embalagem'].widget.attrs.update({'class': 'form-select shadow-none border-0 ps-0 form-control-line'}) 

    class Meta:
        model = remedios
        fields = '__all__'
