from django.contrib import admin

# Register your models here.
from .models import Trivia, Choice

admin.site.register(Trivia)
admin.site.register(Choice)
