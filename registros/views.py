from django.shortcuts import render
from .models import Alumnos
from .models import Tareas

# Create your views here.
def registros(request):
    alumnos = Alumnos.objects.all()
    tareas = Tareas.objects.all()
    return render(request, "registros/principal.html", {"alumnos": alumnos, "tareas": tareas})