# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import fileUpload, NameForm
from django.http import HttpResponseRedirect
from .models import Exam, Login, Set, Analytic, User, Registration, Plan, E_Commerce, Payment, Choose_Plan, Query, Contact_Us, Upload_Form 

#-----------------------------------------------------------------------

def sign_up(request):
    if request.method == "POST":
        form=NameForm(request.POST)
        if form.is_valid:
            return HttpResponseRedirect("/detail/")
    else
       form=NameForm()
    return render(request,"sign_up.html",{'form':form})

#------------------------------------------------------------------------

def home(request):
    home = Plan.objects.all()
    return render(request, 'home.html', {'Name': home,
#                     'Email': Email,
#                     'Password': Password,
#                     'Mobile_no': Mobile_no,
        }
    )

#--------------------------------- Create your views here.---------------

def login(request):
    login = Login.objects.all()
    return render(request, 'login.html', {'latest_upload':login})

#------------------------------------------------------------------------

def blogs(request):
    blog = Query.objects.all()
    return render(request, 'blogs.html', {'Name': blog,
#                     'Email': Email,
#                     'Password': Password,
#                     'Mobile_no': Mobile_no,
        }
    )

#------------------------------------------------------------------------

def discussions(request):
    discussion = Contact_Us.objects.all()
    return render(request, 'discussion.html', {'Name': discussion,
#                     'Email': Email,
#                     'Password': Password,
#                     'Mobile_no': Mobile_no,
        }
    )

#------------------------------------------------------------------------

def promo(request):
    promo = Analytics.objects.all()
    return render(request, 'promo.html', {'Name': promo,
#                     'Email': Email,
#                     'Password': Password,
#                     'Mobile_no': Mobile_no,
        }
    )

#------------------------------------------------------------------------

def refer(request):
    refer = Set.objects.all()
    return render(request, 'refer.html', {'Name': refer,
#                     'Email': Email,
#                     'Password': Password,
#                     'Mobile_no': Mobile_no,
        }
    )

#------------------------------------------------------------------------

def courses(request):
    course = Exam.objects.all()
    return render(request, 'courses.html', {'Name': course,
#                     'Email': Email,
#                     'Password': Password,
#                     'Mobile_no': Mobile_no,
        }
    )

#------------------------------------------------------------------------

def exams(request):
    exam = Exam.objects.all()
    return render(request, 'exams.html', {'Name': exam,
#                     'Email': Email,
#                     'Password': Password,
#                     'Mobile_no': Mobile_no,
        }
    )

#------------------------------------------------------------------------

def passes(request):
    passes = Plan.objects.all()
    return render(request, 'pass.html', {'Name': passes,
#                     'Email': Email,
#                     'Password': Password,
#                     'Mobile_no': Mobile_no,
        }
    )

#------------------------------------------------------------------------

def sign_up(request):
    sign_up = Login.objects.all()
    return render(request, 'sign_up.html', {'Name': sign_up,
#                     'Email': Email,
#                     'Password': Password,
#                     'Mobile_no': Mobile_no,
        }
    )

#------------------------------------------------------------------------

def gk_CA(request):
    Gk_CA = Exam.objects.all()
    return render(request, 'gk_CA.html', {'Name': Gk_CA,
#                     'Email': Email,
#                     'Password': Password,
#                     'Mobile_no': Mobile_no,
        }
    )

#------------------------------------------------------------------------

def practise(request):
    practise = Set.objects.all()
    return render(request, 'practise.html', {'Name': practise,
#                     'Email': Email,
#                     'Password': Password,
#                     'Mobile_no': Mobile_no,
        }
    )

#------------------------------------------------------------------------

def upload(request):
    upload = Upload_Form.objects.all()
    return render(request, 'upload.html', {'Name': upload,
#                     'Email': Email,
#                     'Password': Password,
#                     'Mobile_no': Mobile_no,
        }
    )

#-----------------------------------------------------------------------
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
#------------------------------------------------------------------------

def index(request):
    Name = Registration.objects.all()
    return render(request, 'home.html', {'Name': Name,
#                     'Email': Email,
#                     'Password': Password,
#                     'Mobile_no': Mobile_no,
        }
    )
#-----------------------------------------------------------------------

