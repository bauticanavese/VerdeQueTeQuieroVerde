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

class EventInscription(models.Model):
    person_name = models.CharField(max_length = 200)
    person_email = models.EmailField(max_length = 100)
    event = models.ForeignKey(Event, on_delete = models.CASCADE)

    class Meta:
        unique_together = ['person_name', 'person_email', 'event']

class InscriptionManager:
    @classmethod
    def create_inscription(cls, form, event):
        new_inscription = EventInscription(person_name = form.cleaned_data['name'], person_email = form.cleaned_data['email'], event = event)
        new_inscription.save()
        event.capacity -= 1
        event.save()
