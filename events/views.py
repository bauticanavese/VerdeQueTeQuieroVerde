from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Event

def index(request):
    try:
        page_number = int(request.GET.get('page'))
    except:
        page_number = 1
    events_list = Event.objects.all()
    paginator = Paginator(events_list, 1)
    page_obj = paginator.get_page(page_number)
    context = { 'page_obj' : page_obj }
    return render(request, 'events/index.html', context=context)