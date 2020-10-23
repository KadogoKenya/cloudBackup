from django.conf.urls import url
from . import views

urlpatterns=[
    url('',views.homepage,name = 'home'),
    url(r'^$', views.index, name='index'),
]

