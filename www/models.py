from django.db import models

# Create your models here.
from django.utils import timezone


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    place_of_performance = models.CharField(max_length=200)
    date_of_performance = models.DateTimeField()
    message = models.TextField(max_length=2000)
    date_submitted = models.DateTimeField(default=timezone.now)
