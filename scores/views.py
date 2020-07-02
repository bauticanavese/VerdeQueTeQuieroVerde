from django.shortcuts import render
from django.shortcuts import redirect
from urllib.parse import urlencode
from datetime import date

from .models import Score
from trivias.models import Choice

SCORE_PER_QUESTION = 13


def index(request):
    ranking = Score.objects.order_by('-score')[:10]
    i = 1
    for rank in ranking:
        rank.position = i
        i += 1
    context = {'ranking': ranking}
    return render(request, 'scores/index.html', context=context)


def calculate_score(choices_ids):
    choices = list(map(lambda x: Choice.objects.get(id=x), choices_ids))
    return sum(c.is_correct for c in choices) * SCORE_PER_QUESTION


def create_score(participant, dni, total_score):
    past_scores = Score.objects.filter(dni=dni, play_date__gte=date.today())
    if len(past_scores) > 0:
        raise Exception("Ya participó en la trívia, intente mañana.")

    score = Score(participant=participant, dni=dni, score=total_score)
    score.save()
    return score


def score(request):
    if request.method == 'POST':
        try:
            participant = request.POST.get('name', '')
            dni = request.POST.get('dni', '')
            if not dni:
                raise Exception("Debe ingresar su dni para poder jugar.")
            dni = int(dni)
            selected_choices = {int(v) for (k, v) in request.POST.items() if k.isnumeric()}
            total_score = calculate_score(selected_choices)
            score = create_score(participant, dni, total_score)
        except Exception as e:
            query_string = urlencode({'error_message': e.args[0]})
            url = '/trivias?{}'.format(query_string)
            return redirect(url)

        context = {'participant': score.participant, 'dni': score.dni, 'score': score.score, 'date': score.play_date}

        return render(request, 'scores/score.html', context=context)
    else:
        return redirect('/')
