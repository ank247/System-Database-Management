# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import fileUpload, NameForm
from django.mails import email_sent, BadHeadError
from django.http import HttpResponseRedirect, HttpResponse
from .models import Exam, Login, Set, Analytic, User, Registration, Plan, E_Commerce, Payment, Choose_Plan, Query, Contact_Us, Upload_Form 

def sign_up(request):
    if request.method == "POST":
        form=NameForm(request.POST)
        if form.is_valid:
            return HttpResponseRedirect("/detail/")
    else
       form=NameForm()
    return render(request,"sign_up.html",{'form':form})

def contact_form(request):
       subject=request.POST.get('subject', '')
       message=request.POST.get('message', '')
       sender=request.POST.get('sender', '')
       cc_myself=request.POST.get('cc_myself', '')
       bcc=request.POST.get('bcc','')
       reciepents=['TestLive@edu.in']
       if cc_myself:
          reciepents.append(cc_myself)
       if bcc:
          reciepents.append(bcc)
       if subject and message and sender and reciepents:
          try:
              send.email_sent(subject,message,sender,receipents)
          except BadHeaderError:
            return HttpResponseRedirect("/contact-form/")
       else:
          return HttpResponse("Enter each option again.")
       
def home(request):
    home = Plan.objects.all()
    return render(request, 'home.html', {'Name': home})

def login(request):
    login = Login.objects.all()
    return render(request, 'login.html', {'latest_upload':login})

def blogs(request):
    blog = Query.objects.all()
    return render(request, 'blogs.html', {'Name': blog})

def discussions(request):
    discussion = Contact_Us.objects.all()
    return render(request, 'discussion.html', {'Name': discussion})

def promo(request):
    promo = Analytics.objects.all()
    return render(request, 'promo.html', {'Name': promo})

def refer(request):
    refer = Set.objects.all()
    return render(request, 'refer.html', {'Name': refer})

def courses(request):
    course = Exam.objects.all()
    return render(request, 'courses.html', {'Name': course})

def exams(request):
    exam = Exam.objects.all()
    return render(request, 'exams.html', {'Name': exam})

def passes(request):
    passes = Plan.objects.all()
    return render(request, 'pass.html', {'Name': passes,
        }
    )

def gk_CA(request):
    Gk_CA = Exam.objects.all()
    return render(request, 'gk_CA.html', {'Name': Gk_CA})

def practise(request):
    practise = Set.objects.all()
    return render(request, 'practise.html', {'Name': practise})

def upload(request):
    upload = Upload_Form.objects.all()
    return render(request, 'upload.html', {'Name': upload})

"""
def file_upload(request):
  if request.method == 'POST': 
     form = fileUpload(request.POST, request.FILES)
     if form.is_valid():
        handle_fileUpload(request.FILES['file'])
        return HttpResponseRedirect('/success/url/')
  else:
      form = fileUpload()
  return render(request, 'detail.html', {'form' : form})
"""

def index(request):
    Name = Registration.objects.all()
    return render(request, 'home.html', {'Name': Name})

