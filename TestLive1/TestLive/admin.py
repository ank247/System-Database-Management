# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import EmailModel,Profile


admin.site.register(EmailModel)
admin.site.register(Profile)

