from django.db import models
from ws17 import settings
from django import forms

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=127)
    birthday = models.DateField()
    age = models.IntegerField()
    
    def __str__(self):
        return self.name