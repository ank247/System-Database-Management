
from django import forms
from django.db import models
from .models import SignUp, Login

class NameForm(forms.Form):
    
    
class ContactForm(forms.Form):
    subject=forms.CharField(max_length=100)
    message=forms.CharField(widget=forms.Textarea,max_length=300)
    sender=forms.EmailField()
    cc_myself=forms.BooleanField(required=False)
    bcc=forms.EmailField()
    
class fileUpload(forms.Form):
    title = forms.CharField(max_length = 30)
    file = forms.FileField()

class Exam(forms.Form):
    Exam_Type = forms.FileField()
    file = forms.FileField()
    
