
from django.conf.urls import url
from .views import blogList


urlpatterns=[
   url('',blogList.as_view(template_name='blogs/blogList.html'),name='blogList'),
]
