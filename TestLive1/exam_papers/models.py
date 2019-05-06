# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Group

class Physic(models.Model):
      course=models.CharField(max_length=100)
      paper_id=models.CharField(max_length=50)
      paper=models.CharField(max_length=50)

      def __str__(self):
          return self.course

class Chemistry(models.Model):
      course=models.CharField(max_length=100)
      paper_id=models.CharField(max_length=50)
      paper=models.CharField(max_length=50)

      def __str__(self):
          return self.course

class Mathematic(models.Model):
      course=models.CharField(max_length=100)
      paper_id=models.CharField(max_length=50)
      paper=models.CharField(max_length=50)

      def __str__(self):
          return self.course

class Mechanical(models.Model):
      course=models.CharField(max_length=100)
      paper_id=models.CharField(max_length=50)
      paper=models.CharField(max_length=50)

      def __str__(self):
          return self.course

class Computer_Science(models.Model):
      course=models.CharField(max_length=100)
      paper_id=models.CharField(max_length=50)
      paper=models.CharField(max_length=50)

      def __str__(self):
          return self.course

class Electrical(models.Model):
      course=models.CharField(max_length=100)
      paper_id=models.CharField(max_length=50)
      paper=models.CharField(max_length=50)

      def __str__(self):
          return self.course

class Electronic(models.Model):
      course=models.CharField(max_length=100)
      paper_id=models.CharField(max_length=50)
      paper=models.CharField(max_length=50)

      def __str__(self):
          return self.course

class Civil(models.Model):
      course=models.CharField(max_length=100)
      paper_id=models.CharField(max_length=50)
      paper=models.CharField(max_length=50)

      def __str__(self):
          return self.course

