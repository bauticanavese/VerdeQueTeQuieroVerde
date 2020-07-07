from django.db import models
from django.utils import timezone

MAX_SIZE_CONTENT_LIST = 200


class Material(models.Model):
    DEFAULT_IMG = 'http://www.lavozdecataratas.com/contenido/fotos/05062020_073730.jpg'

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400, default='material description')
    creation_date = models.DateTimeField('date published', default=timezone.now)
    content = models.TextField(max_length=5000, default='material content')
    attached_document = models.URLField()
    img_url = models.URLField(default=DEFAULT_IMG)

    def __str__(self):
        return self.title
    
    def resume(self):
        if len(self.content) > MAX_SIZE_CONTENT_LIST:
            self.content = f'{self.content[:MAX_SIZE_CONTENT_LIST]}...'
        self.creation_date = self.creation_date.date()
