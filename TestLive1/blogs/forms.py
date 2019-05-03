
from django import forms
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import BlogModel
 
class BlogForm(forms.Form):
      blog=forms.CharField(max_length=500)            
      class Meta:
            model=BlogModel
            tables=['user','blog']
            

