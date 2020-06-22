from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:material_id>', views.show_material, name='show_material')
]
