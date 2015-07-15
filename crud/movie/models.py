from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    funny = models.BooleanField(default=True)
