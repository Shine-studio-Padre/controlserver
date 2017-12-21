from django.conf.urls import url, include
from control import views

urlpatterns = [
    url(r'^account/$', views.account, name='account'),
    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
    url(r'^registr/', views.register),
    url(r'^$', views.index, name='index'),
]
