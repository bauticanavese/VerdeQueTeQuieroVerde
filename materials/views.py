from django.shortcuts import render
from .models import Material
from django.http import HttpResponse

def transform_to_view(material):
    material.resume()
    return material

def index(request):
    materials = map(transform_to_view, Material.objects.all())
    context = { 'materials' : materials }
    return render(request, 'materials/index.html', context=context)

def show_material(request, material_id):
    material = Material.objects.get(id=material_id)
    context = { 'material' : material }
    return render(request, "materials/show_material.html", context=context)
