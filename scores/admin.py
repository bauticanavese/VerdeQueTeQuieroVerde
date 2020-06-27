from django.contrib import admin

from .models import Score

class ScoreAdmin(admin.ModelAdmin): 
    list_display = ('dni', 'play_date')

admin.site.register(Score, ScoreAdmin)
