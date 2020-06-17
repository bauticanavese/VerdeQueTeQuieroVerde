from django.db import models


class Prize(models.Model):
    prize_title = models.CharField(max_length=50)
    points_required = models.IntegerField(default=0)

    def __str__(self):
        return self.prize_title
