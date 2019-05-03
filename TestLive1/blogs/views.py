# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import BlogForm 
from .models import BlogModel

# Create your views here.

def blogs(request):
    blog=BlogModel()
    return render(request,'blogs/blogs.html',{'blogs':blog})

"""
def blogs(request):
    if request.method=="POST":
       blogs=BlogForm(request.POST)
       if blogs.is_valid():
          blogs.save()
          return HttpResponseRedirect('/blogs/')
    else:
       blogs=BlogForm()
    return HttpResponse(request,'blogs/blogs.html',{'blogs':blogs})
"""

