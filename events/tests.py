from django.test import TestCase

from .models import Event


class EventModel(TestCase):
    def test_name(self):
        event = Event(title='First event')
        self.assertIs(event.title, 'First event')

    def test_default_fields(self):
        event = Event(title='Event')
        self.assertIs(event.capacity, 0)
        self.assertIs(event.title, 'Event')
        self.assertEqual(event.place, 'event place')
        self.assertEqual(event.topic, 'event topic')
