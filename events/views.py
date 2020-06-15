from django.shortcuts import render
from .models import Event

def index(request):
    post_per_page = 5
    try:
        page_number = int(request.GET.get('page'))
        index = page_number*post_per_page - 1
    except:
        index = 0
    events = Event.objects.all()[index:index+post_per_page]
    visited = index * post_per_page + post_per_page
    has_more = True if(Event.objects.all().count() > visited) else False
    context = { 'events_list' : events , 'has_more' : has_more }
    return render(request, 'events/index.html', context=context)
