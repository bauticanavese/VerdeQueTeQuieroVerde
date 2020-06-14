from django.shortcuts import render
from .models import Event

def index(request):
    events = Event.objects.all()[:5]
    context = { 'events_list' : events }
    return render(request, 'events/index.html', context=context)
