
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import EmailModel,Profile


class UserRegistrationForm(UserCreationForm):
      email=forms.EmailField()
      
      class Meta:
            model=User
            fields=['username','email','password1','password2']


class EmailForm(ModelForm):
      to_email=forms.EmailField()      
      class Meta:
            model=EmailModel
            fields=['subject','message','from_email','to_email']      


class UserUpdateForm(ModelForm):
      email=forms.EmailField()

      class Meta:
            model=User
            fields=['username','email']


class ProfileUpdateForm(ModelForm):
      class Meta:
            model=Profile
            fields=['image']


