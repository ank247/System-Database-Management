"""TestLive1 URL Configuration

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

from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django import views
from django.contrib.auth import views as auth_view
from TestLive import views as TestLive_view
from TestLive.syndicate import LatestEntries
from blogs import views as blog_view,urls as blog_url
from payment import views as payment_view
from exam_papers import views as examPaper_view
from emails import views as email_view



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('login/',auth_view.LoginView.as_view(template_name='TestLive/login.html'),name='login'),
    url('logout/',auth_view.LogoutView.as_view(template_name='TestLive/logout.html'),name='logout'),
    url('feeds/',LatestEntries(),name='feeds'),
    url('',include(blog_url),name='blog'),
]



urlpatterns+=[
   url('register/',TestLive_view.register,name='register'),
   url('profile/',TestLive_view.profile,name='profile'),
   url('csv_view/',TestLive_view.csv_view,name='csv_view'),
]



urlpatterns+=[
   url('exam_paper/',examPaper_view.paper,name='paper'),
   url('email/',email_view.send_email,name='emails'),
   url('payment/',payment_view.payment,name='payment'),
]



urlpatterns+=[
   url('',blog_view.update_blog,name='blog'),
]



if settings.DEBUG:
   urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

