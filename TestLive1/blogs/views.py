# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .forms import blogForm
from .models import blogModel


class blogList(ListView):
    model=blogModel


@login_required
def update_blog(request):
    if request.method=='POST':
       blog=blogForm(request.POST,instance=request.user)       
       if blog.is_valid():
          blog.save()
          #user=form.cleaned_data.get('username')
          return HttpResponseRedirect('/blogs/blog/')
    else:
       blog=blogForm(instance=request.user)
    return render(request,'blogs/blogs.html',{'blog':blog})

