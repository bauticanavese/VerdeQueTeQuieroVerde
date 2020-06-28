from django.test import TestCase
from .models import Score

class ScoreModel(TestCase):
    def test_participant(self):
      score = Score(participant='Pepe Suarez')
      self.assertIs(score.participant, 'Pepe Suarez')

    def test_default_fields(self):
      score = Score(participant='Pepe Suarez')
      self.assertIs(score.score, 0)
      self.assertIs(score.dni, 0)
    
    def test_play_date_is_none(self):
      score = Score(participant='Pepe Suarez')
      self.assertIs(score.play_date, None)
    
    def test_play_date_is_none_until_save_score(self):
      score = Score(participant='Pepe Suarez')
      score.save()
      self.assertTrue(score.play_date)