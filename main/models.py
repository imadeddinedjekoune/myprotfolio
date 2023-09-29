from django.db import models

# Create your models here.
class Visitors(models.Model):
    ip = models.CharField(max_length=100)
    info = models.CharField(max_length=200)


class Emails(models.Model):
    send_name = models.CharField(max_length=200)
    send_email = models.CharField(max_length=200)
    send_context = models.CharField(max_length=200)

