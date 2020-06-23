from django.db import models

# Create your models here.
class Trivia(models.Model):
    title = models.CharField(max_length = 100, default = 'Trivia title')

    def __str__(self):
        return "%s" % self.title

class Choice(models.Model):
    trivia = models.ForeignKey(Trivia, on_delete = models.CASCADE)
    text = models.CharField(max_length = 100, default = 'Trivia choice')
    is_correct = models.BooleanField(default = False)

    def __str__(self):
        return "%s" % self.text
