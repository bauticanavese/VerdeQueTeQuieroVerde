from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Event, EventInscription, InscriptionManager
from .forms import EventForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

def index(request):
    try:
        page_number = int(request.GET.get('page'))
    except:
        page_number = 1
    events_list = Event.objects.all()
    paginator = Paginator(events_list, 1)
    page_obj = paginator.get_page(page_number)
    context = { 'page_obj' : page_obj }
    return render(request, 'events/index.html', context = context)

def register_form(request):
    if request.method == 'GET':
        form = EventForm()
        event_id = request.GET.get('id', 0)
        context = { "form" : form , "id" : event_id }
        return render(request, 'events/register_form.html', context = context)
    else:
        form = EventForm(request.POST)
        if form.is_valid():
            event_id = int(request.POST.get('event_id'))
            event = Event.objects.get(id = event_id)
            try:
                InscriptionManager.create_inscription(form, event)
                messages.success(request, 'Ud. se inscribio correctamente')
                return redirect('/events/')
            except:
                messages.error(request, 'Ud. no pudo inscribirse')
                return redirect('/events/')
