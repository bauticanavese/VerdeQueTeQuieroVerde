from django.shortcuts import render

def index(request):
    my_dict = {'saludo':"Hello from events view!!!"}
    return render(request, 'events/index.html', context=my_dict)
