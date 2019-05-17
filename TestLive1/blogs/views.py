# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.core.paginator import Paginator
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
          return HttpResponseRedirect('/blogs/')
    else:
       blog=blogForm(instance=request.user)
    return render(request,'blogs/blogs.html',{'blog':blog})



def list_blog(request):
    blog=blogModel.objects.all()
    p=Paginator(blog,1)
    page=request.GET.get('page',1)
    p1=p.page(page)
    return render(request,'blogs/blogList.html',{'page':p1})    
    

