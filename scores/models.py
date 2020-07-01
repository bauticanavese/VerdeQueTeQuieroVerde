from django.db import models


class Score(models.Model):
    participant = models.CharField(max_length=200, default='')
    dni = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    play_date = models.DateTimeField('play date', auto_now=True)

    def __str__(self):
        return f"{self.dni}-{self.play_date.date()}"
