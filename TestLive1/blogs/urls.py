
from django.conf.urls import url
from django import views
from . import views 

urlpatterns=[
   url('',views.blogs,name='blogs'),
]

