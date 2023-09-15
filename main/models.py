from django.db import models

# Create your models here.
class Visitors(models.Model):
    ip = models.CharField(max_length=100)
    info = models.CharField(max_length=200)
