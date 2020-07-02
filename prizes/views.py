from django.shortcuts import render
from .models import Prize


def index(request):
    prizes = Prize.objects.order_by('-points_required')
    context = { 'prizes' : prizes }
    return render(request, 'prizes/index.html', context = context)
