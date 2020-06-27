from django.shortcuts import render
from .models import Trivia

def index(request):
  trivias = Trivia.objects.all()
  context = {'trivias': trivias}
  return render(request, 'trivias/index.html', context=context)
