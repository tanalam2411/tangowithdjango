'''
Created on Jun 14, 2015

@author: tanveer
'''


from django.conf.urls import  url
from rango import views


urlpatterns = [
        url(r'^$', views.index, name='rango-index'),
        url(r'^about/', views.about, name='rango-about'),       
        ]

