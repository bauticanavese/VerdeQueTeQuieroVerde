from django.db import models


class Workgroup(models.Model):
    name = models.CharField(max_length=100)
    topic = models.CharField(max_length=200, default='workgroup topic')
    supervisor = models.CharField(max_length=50, default='workgroup supervisor')
    number_of_participants = models.IntegerField(default=0)

    def __str__(self):
        return self.name
