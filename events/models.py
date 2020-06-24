from django.db import models
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date published', default=timezone.now)
    event_date = models.DateTimeField('date event', default=timezone.now)
    topic = models.CharField(max_length=200, default='event topic')
    capacity = models.IntegerField(default=0)
    place = models.CharField(max_length=100, default='event place')

    def __str__(self):
        return self.title
