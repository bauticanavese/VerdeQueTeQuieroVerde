from django.test import TestCase

# Create your tests here.
from .models import Prize

class PrizeModel(TestCase):
    def test_name(self):
        prize = Prize(prize_title='A Reward')
        self.assertIs(prize.prize_title, 'A Reward')

    def test_default_fields(self):
        prize = Prize(prize_title='A Reward')
        self.assertIs(prize.points_required, 0)
