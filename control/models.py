from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserServer(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=None)
    folder = models.CharField(max_length=255, blank=True, null=True, default=None)

class UserFunction(models.Model):
    user = models.ForeignKey(UserServer, blank=True, null=True, default=None)
    new = models.CharField(max_length=255, blank=True, null=True, default=None)
    delete = models.CharField(max_length=255, blank=True, null=True, default=None)
    edit = models.CharField(max_length=255, blank=True, null=True, default=None)
