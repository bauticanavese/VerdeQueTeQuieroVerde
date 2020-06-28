from django.contrib import admin

# Register your models here.
from .models import Event, EventInscription

admin.site.register(Event)
admin.site.register(EventInscription)
