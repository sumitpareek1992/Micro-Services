from django.db import models
from django.contrib.auth.models import User




class AccountUser(models.Model):
    first_name = models.CharField(max_length=200,null=True,blank=True)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    email = models.CharField(max_length=200,unique=True,null=True,blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    password2 = models.CharField(max_length=100, null=True, blank=True)
