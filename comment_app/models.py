from django.db import models
from django.db.models.expressions import F
from django.db.models.fields import EmailField
from django_mysql.models import ListCharField
from django.contrib.auth.models import User
from django import forms
# Create your models here.

class users(models.Model):
    id=models.AutoField(primary_key=True)
    Email=models.EmailField(max_length=100,unique=True)
    password=models.CharField(max_length=100)
    screct=models.CharField(max_length=100)