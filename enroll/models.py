from django.db import models
from django.forms import ModelForm


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)