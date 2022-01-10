from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    place_of_performance = models.CharField(max_length=200)
    date_of_performance = models.DateTimeField()
    message = models.TextField(max_length=2000)
    date_submitted = models.DateTimeField(default=timezone.now)


class EventManager(models.Manager):
    """ Event manager """

    def get_all_events(self):
        events = Event.objects.filter(is_active=True, is_deleted=False)
        return events

    def get_running_events(self):
        running_events = Event.objects.filter(
            is_active=True,
            is_deleted=False,
            end_time__gte=datetime.now().date(),
        ).order_by("start_time")
        return running_events


class EventAbstract(models.Model):
    """ Event abstract model """

    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Event(EventAbstract):
    """ Event model """
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    objects = EventManager()

    def __str__(self):
        return self.title
