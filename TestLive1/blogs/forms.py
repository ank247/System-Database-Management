
from django.forms import ModelForm
from .models import blogModel
from django import forms


class blogForm(ModelForm):
    email=forms.EmailField()
    class Meta:
        model=blogModel
        fields=['email','title','blog']

