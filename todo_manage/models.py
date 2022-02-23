from email.policy import default
from turtle import title
from xmlrpc.client import Boolean
from django.db import models
from django.forms import BooleanField

# Create your models here.
class Todo(models.Model):
  title=models.CharField(max_length=100)
  desc=models.TextField()
  completed=models.BooleanField(default=False)
  
  def __str__(self):
        return self.title