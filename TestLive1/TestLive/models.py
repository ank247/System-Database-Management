# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models

from django.contrib.auth.models import User


class EmailModel(models.Model):
      subject=models.CharField(max_length=100)
      message=models.CharField(max_length=10000)
      from_email=models.OneToOneField(User,on_delete=models.CASCADE)
      to_email=models.EmailField()

      def __str__(self):
          return self.from_email.username     


class Profile(models.Model):
      user=models.OneToOneField(User,on_delete=models.CASCADE)
      image=models.ImageField(default='default.jpg',upload_to='profile_pics')

      def __str__(self):
          return self.user.username


