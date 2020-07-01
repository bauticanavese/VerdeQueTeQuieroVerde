from django.shortcuts import render

from .models import Workgroup


def index(request):
    workgroups = Workgroup.objects.all()
    context = {'workgroups': workgroups}
    return render(request, 'workgroups/index.html', context=context)
