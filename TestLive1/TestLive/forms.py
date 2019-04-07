
from django import forms
from django.db import models
from .models import SignUp, Login

class NameForm(forms.Form):
    
    
class ContactForm(forms.Form):
    sender=forms.EmailField(max_length=50)
    text=forms.CharField(required=textarea,max_length=300)
    cc_sender=forms.EmailField(max_length=50)
    receipients=forms.EmailField(max_length=50)
    
class fileUpload(forms.Form):
    title = forms.CharField(max_length = 30)
    file = forms.FileField()

class Exam(forms.Form):
    Exam_Type = forms.FileField()
    file = forms.FileField()

