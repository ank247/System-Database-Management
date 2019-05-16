# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class blogModel(models.Model):
      user=models.TextField(max_length=150)
      date=models.DateTimeField()
      title=models.CharField(max_length=150)
      blog=models.CharField(max_length=1000)
      
      class Meta:
          ordering=["user"]

      def __str__(self):
          return self.title


"""
@receiver(post_save,sender=User)
def create_user_blog(sender,instance,created,**kwargs):
    if created:
       blogModel.objects.create(title=instance)


@receiver(post_save,sender=User)
def save_user_blog(sender,instance,**kwargs):
    instance.blogmodel.save()

"""
