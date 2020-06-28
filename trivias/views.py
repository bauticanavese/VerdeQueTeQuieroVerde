from django.shortcuts import render
from django.http import HttpResponse
from .models import Trivia
from .models import Choice

def index(request):
  error_message = request.GET.get('error_message', '')
  trivias = Trivia.objects.all()
  choices = Choice.objects.all()
  context = {'trivias': trivias, 'choices': choices, 'error': error_message}

  return render(request, 'trivias/index.html', context=context)