from django.db import models
from django.utils import timezone


class Material(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400, default='material description')
    creation_date = models.DateTimeField('date published', default=timezone.now)
    content = models.TextField(max_length=5000, default='material content')
    attached_document = models.URLField()

    def __str__(self):
        return self.title
    
    def resume(self):
        if len(self.content) > 80:
            self.content = f'{self.content[:80]}...'
        self.creation_date = self.creation_date.date()