from django.test import TestCase

# Create your tests here.
from .models import Trivia, Choice

class EventModel(TestCase):
    def test_trivia(self):
        trivia = Trivia(title = 'First trivia')
        self.assertEqual(str(trivia), 'First trivia')

    def test_false_choice(self):
        trivia = Trivia(title = 'Second trivia')
        choice = Choice(text = 'first choice', trivia = trivia, is_correct = False)
        self.assertEqual(str(choice), 'first choice')
        self.assertIs(choice.trivia, trivia)
        self.assertIs(choice.is_correct, False)

    def test_multiple_choices(self):
        trivia = Trivia(title = 'Second trivia')
        choice = Choice(text = 'first choice', trivia = trivia, is_correct = True)
        self.assertIs(choice.is_correct, True)
        choice = Choice(text = 'second choice', trivia = trivia, is_correct = True)
        self.assertIs(choice.is_correct, True)
        choice = Choice(text = 'third choice', trivia = trivia, is_correct = False)
        self.assertIs(choice.is_correct, False)

    def test_delete_trivia_cascade(self):
        trivia = Trivia(title = 'delete trivia')
        trivia.save()
        trivia_id = trivia.id
        choice = Choice(text = 'delete choice', trivia = trivia, is_correct = True)
        choice.save()
        choice_id = choice.id
        trivia.delete()
        with self.assertRaises(Choice.DoesNotExist):
            Choice.objects.get(id = choice_id)
        with self.assertRaises(Trivia.DoesNotExist):
            Trivia.objects.get(id = trivia_id)
