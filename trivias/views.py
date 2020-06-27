from django.shortcuts import render
from django.http import HttpResponse
from .models import Trivia
from .models import Choice

def index(request):
  trivias = Trivia.objects.all()
  choices = Choice.objects.all()
  context = {'trivias': trivias, 'choices': choices}
  return render(request, 'trivias/index.html', context=context)