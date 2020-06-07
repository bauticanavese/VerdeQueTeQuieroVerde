from django.test import TestCase

# Create your tests here.
from .models import Event

class EventModel(TestCase):
    def test_name(self):
        event = Event(title = 'First event')
        self.assertIs(event.title, 'First event')
