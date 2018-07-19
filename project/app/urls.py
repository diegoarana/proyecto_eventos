from django.conf.urls import url, include
from rest_framework import routers
from . import views as evento

urlpatterns = [
    url(r'^index/$', evento.index, name='index'),
]