from django.shortcuts import render
from django.http import HttpResponse

from .models import Score
from trivias.models import Choice

SCORE_PER_QUESTION = 5

def calculate_score(choices_ids):
  choices = list(map(lambda x: Choice.objects.get(id=x), choices_ids))
  return sum(c.is_correct for c in choices)*SCORE_PER_QUESTION

def create_score(participant, dni, total_score):
  score = Score(participant=participant, dni=dni, score=total_score)
  score.save()
  return score

def score(request):
  if request.method == 'POST':
    participant = request.POST.get('name', '')
    dni = int(request.POST.get('dni', ''))
    selected_choices = { int(v) for (k,v) in request.POST.items() if k.isnumeric()}
    total_score = calculate_score(selected_choices)
    score = create_score(participant, dni, total_score)
    
    context = {'participant': score.participant, 'dni': score.dni, 'score': score.score, 'date': score.play_date}

    return render(request, 'scores/score.html', context=context)
  else:
    return HttpResponse()
