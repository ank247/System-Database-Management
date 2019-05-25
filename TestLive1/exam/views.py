# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator
from .models import paper


def paper_view(request):
    if paper.type=="IIT_Advance":
       p=paper.objects.get(type="IIT_Advance")
    elif paper.type=="IIT_Mains":
       p=paper.objects.get(type="IIT_Mains")
    elif paper.type=="Gate_Mains":
       p=paper.objects.get(type="IIT_Mains")
    elif paper.type=="Gate_ME":
       p=paper.objects.get(type=="IIT_Mains")
    elif paper.type=="IIT_Mains":
       p=paper.objects.get(type=="IIT_Mains")
    else:
       p=paper.objects.get(type=="IIT_Mains")
    p1=Paginator(p,10)
    page=request.GET.get('page',1)
    p1=p1.page(page)
    return render(request,'exam/exam1.html',{'page':p1})
    
     

