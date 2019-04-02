
from django import forms
from django.db import models

class fileUpload(forms.Form):
    title = forms.CharField(max_length = 30)
    file = forms.FileField()

class Exam(forms.Form):
    Exam_Type = forms.FileField()
    file = forms.FileField()

