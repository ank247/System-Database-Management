
from django.conf.urls import url
from .views import blogList
from . import views


urlpatterns=[
   #url('',blogList.as_view(template_name='blogs/blogList.html'),name='blogList'),
   url('',views.list_blog,name='list_blog'),
]


