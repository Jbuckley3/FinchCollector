from django import forms
from .models import Finch

class FinchForm(forms.ModelForm):
    class Meta:
        model = Finch
        fields = ['name', 'color', 'size']
       
