"""TestLive0 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

app_name = 'TestLive'

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^TestLive/login/$', views.login, name = 'login'),
    url(r'^TestLive/blogs/$', views.blogs, name='blogs'),
    url(r'^TestLive/discussion/$', views.discussions, name = 'discussion'),
    url(r'^TestLive/promo/$', views.promo, name='promo'),
    url(r'^TestLive/refer/$', views.refer, name = 'refer'),
    url(r'^TestLive/courses/$', views.courses, name = 'course'),
    url(r'^TestLive/exams/$', views.exams, name='exam'),
    url(r'^TestLive/home/$', views.home, name = 'home'),
    url(r'^TestLive/pass/$', views.passes, name='passes'),
    url(r'^TestLive/sign_up/$', views.sign_up, name = 'sign_up'),
    url(r'^TestLive/gk_CA/$', views.gk_CA, name='gk_CA'),
    url(r'^TestLive/practise/$', views.practise, name = 'practise'),
    url(r'^TestLive/upload/$', views.upload, name='upload'),

]

