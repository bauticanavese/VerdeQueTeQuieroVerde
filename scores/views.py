from django.shortcuts import render
from django.http import HttpResponse

from trivias.models import Choice

SCORE_PER_QUESTION = 5

def calculate_score(choices_ids):
    choices = list(map(lambda x: Choice.objects.get(id=x), choices_ids))
    print(choices)
    return sum(c.is_correct for c in choices)*SCORE_PER_QUESTION

def score(request):
  if request.method == 'POST':
    selected_choices = { int(v) for (k,v) in request.POST.items() if k.isnumeric()}
    score = calculate_score(selected_choices)
    print(request.POST)
    print(score)
    context = {'score': score}

    return render(request, 'scores/score.html', context=context)
  else:
    return HttpResponse()
