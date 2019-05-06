# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class emails(models.Model):
      subject=models.CharField(max_length=100)
      message=models.CharField(max_length=1000)
      from_email=models.EmailField()
      user=models.OneToOneField(User,on_delete=models.CASCADE)
      to_email=models.EmailField()
      
      def __str__(self):
          return self.user.username
     
    
