from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from django.conf import settings

import loginsys
from loginsys import views
urlpatterns = [
    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
]