from django.db import models
from django.core import validators as v
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50,validators=[v.MinLengthValidator(4),
        v.MaxLengthValidator(10)])
    division=models.IntegerField(max_length=50,)
    admsn_no=models.IntegerField(max_length=50,)
    place=models.CharField(max_length=100,)
    phone=models.IntegerField(max_length=10,)

class Teacher(models.Model):
    name=models.CharField(max_length=50,)
    department=models.CharField(max_length=50,)
    email=models.CharField(max_length=50,)
