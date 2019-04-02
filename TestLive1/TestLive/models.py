# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms
#from .forms import fileUpload
# Create your models here.

class Exam(models.Model):
    Exam_Type = models.CharField(max_length = 30)
    Date = models.DateTimeField('date published')
    
    def __Exam__(self):
        return self.Exam_Type

class Set(models.Model):
    GATE = models.ImageField()
    SSC = models.ImageField()
    RRB = models.ImageField()
    RAILWAY = models.ImageField()
    BANK = models.ImageField()

class Analytic(models.Model):
    Analytic = models.ImageField()

class User(models.Model):
    Username = models.CharField(max_length = 100)
    Email_Address = models.CharField(max_length = 100)
    Contact_Detail = models.DecimalField(max_digits = 10, decimal_places=0)
    Profile_Pic = models.ImageField()
    Temporary_Address = models.CharField(max_length = 150)
    PAN = models.DecimalField(max_digits = 16, decimal_places = 0)
    Aadhar_Card = models.DecimalField(max_digits = 16, decimal_places = 0)
    start_date = models.DateField('Start Date')
    end_date = models.DateField('End Date')
   
class Registration(models.Model):
    Name = models.CharField(max_length = 100)
    Email = models.CharField(max_length = 100)
    Password = models.CharField(max_length = 1000)
    Mobile_no = models.DecimalField(max_digits = 10, decimal_places = 0)

class Login(models.Model):
    Email = models.CharField(max_length = 100)
    Password = models.CharField(max_length = 128)

class Plan(models.Model):
    Plan = models.CharField(max_length = 30)
#    Paid = models.CharField(max_length = 30)

class E_Commerce(models.Model):
    E_Commerce = models.CharField(max_length = 30)
#    Credit = models.CharField(max_length = 32)
#    Neft = models.CharField(max_length = 50)

class Payment(models.Model):
    Coupon = models.CharField(max_length = 32)
    Draft = models.CharField(max_length = 50)
    Cash_Deposit = models.CharField(max_length = 50)
    Echallan = models.CharField(max_length = 50)

class Choose_Plan(models.Model):
    select_plan = models.ForeignKey(Plan)

class Query(models.Model):
    query = models.CharField(max_length = 15)
#    Comment = models.CharField(max_length = 100)
#    Other = models.CharField(max_length = 150)

class Contact_Us(models.Model):
    Name = models.CharField(max_length = 100)
    Email = models.CharField(max_length = 100)
    Phone = models.DecimalField(max_digits = 10, decimal_places = 0)
    Subject = models.ForeignKey(Query)
    Message = models.CharField(max_length = 150)

class Upload_Form(models.Model):
    Form = models.FileField()

