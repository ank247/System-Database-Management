
from django.conf.urls import url
from . import views

urlpatterns=[
   url('exam/',views.paper_view,name='paper_view'),
]
