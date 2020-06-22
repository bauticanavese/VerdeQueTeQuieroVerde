from django.shortcuts import render
from .models import Material

def transform_to_view(material):
    material.resume()
    return material

def index(request):
    materials = map(transform_to_view, Material.objects.all())
    context = { 'materials' : materials }
    return render(request, 'materials/index.html', context=context)

