from django.db import models

# Create your models here.
class Mainmodule(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    task=models.CharField(max_length=100)
    tasktime=models.CharField(max_length=100)
