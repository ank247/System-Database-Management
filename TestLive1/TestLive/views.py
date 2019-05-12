#-*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,StreamingHttpResponse
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm,EmailForm,ProfileUpdateForm,UserUpdateForm
from .models import Profile
from django.core.mail import BadHeaderError,send_mail
import csv
from django.template import Context,loader
from .models import Exam, Login, Set, Analytic, User, Registration, Plan, E_Commerce, Payment, Choose_Plan, Query, Contact_Us, Upload_Form 
from .forms import fileUpload, NameForm


def register(request):
    if request.method=='POST':
       form=UserRegistrationForm(request.POST)
       if form.is_valid():
          form.save()
          username=form.cleaned_data.get("username")
          return HttpResponseRedirect('')
    else:
        form=UserRegistrationForm()
    return render(request,'TestLive/register.html',{'form':form})



@login_required
def profile(request):
    try:
        profile=request.user.profile
    except Profile.DoesNotExist:
        profile=Profile(user=request.user)
    if request.method=='POST':
       u_form=UserUpdateForm(request.POST,instance=request.user)
       p_form=ProfileUpdateForm(request.POST or None,request.FILES,instance=profile)
       if u_form.is_valid() and p_form.is_valid():
          p_form.save()
          u_form.save()
          return HttpResponseRedirect('')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)

    context={
             'u_form':u_form,
             'p_form':p_form
            }
    return render(request,'TestLive/profile.html',context) 


def feeds(request):
    return render(request,'TestLive/feeds.html')

"""
def send_email(request):
    if request.method=='POST':
       email_form=EmailForm(request.POST)
       if email_form.is_valid():
          email_form.save()
          send_mail('subject','message','email_form.from_email',['to_email@gmail.com'],fail_silently=False)
          return HttpResponse('Hello')  
    else:
        #email_form=EmailForm()
        return HttpResponse("Enter Valid Form")
    return redirect(request,'TestLive/email.html',{'email':email_form})
"""    



def send_email(request):
    if request.method=='POST':
       subject = request.POST.get(request.POST,'subject', '')
       message = request.POST.get('message', '')
       from_email = 'TestLive@ac.in'
       if subject and message and from_email:
          try:
              send_mail(subject, message, from_email, ['admin@example.com'])
          except BadHeaderError:
              return HttpResponse('Invalid header found.')
          return HttpResponseRedirect('')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')
    return redirect(request,'TestLive/email.html')



class Echo():
      def write(self,value):
          return value


def csv_view(request):
    """
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment;filename="Charan_PG.xlsx"'
    csv_data=(
        ('First row','Foo','Bar','Baz'),
        ('Second row','A','B','Testing'),
    )
    
    t=loader.get_template('csv_to_txt.txt')
    c=Context({
      'data':csv_data,
    })
    response.write(t.render(c))
    return response

    """
    rows=(["Row {}".format(idx),str(idx)] for idx in range(65536))
    pseudo_buffer=Echo()
    writer=csv.writer(pseudo_buffer)
    response=StreamingHttpResponse((writer.writerow(row) for row in rows),content_type="text/csv")
    response['Content-Disposition']='attachment;filename="Charan_PG.xlsx"'
    return response


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
          reciepents.append(sender)
       if bcc:
          reciepents.append(bcc)
       if subject and message and sender and reciepents:
          try:
              send_email(subject,message,sender,receipents)
              return HttpResponseRedirect("/home/contactform")
          except BadHeaderError:
            return HttpResponse("failed")
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
    return render(request, 'pass.html', {'Name': passes})

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

