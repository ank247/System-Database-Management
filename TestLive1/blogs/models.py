# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class BlogModel(models.Model):
      user=models.ForeignKey(User,on_delete=models.CASCADE)
      blog=models.CharField(max_length=250)
    
      def __str__(self):
          return self.user.username

