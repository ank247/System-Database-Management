# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class payment(models.Model):
      account_no=models.IntegerField()
