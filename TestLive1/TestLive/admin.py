# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

class modelAdmin(admin.ModelAdmin):
    fields = ['Exam_Type', 'Type']

# Register your models here.

# Type: ~/TestLive1/TestLive/models.py

from .models import Exam
admin.site.register(Exam)

from .models import User
admin.site.register(User)

from .models import Registration
admin.site.register(Registration)

from .models import Login
admin.site.register(Login)

from .models import Plan
admin.site.register(Plan)

from .models import E_Commerce
admin.site.register(E_Commerce)

from .models import Payment
admin.site.register(Payment)

from .models import Choose_Plan
admin.site.register(Choose_Plan)

from .models import Analytic
admin.site.register(Analytic)

from .models import Contact_Us
admin.site.register(Contact_Us)

from .models import Query
admin.site.register(Query)

from .models import Set
admin.site.register(Set)

from .models import Upload_Form
admin.site.register(Upload_Form)

#from .forms import fileUpload
#admin.site.register(fileUpload)

#-------------------------------------------------------------------------

#Type: ~/TestLive1/TestLive/forms.py
"""
from .forms import Exam
admin.site.register(Exam)
"""
