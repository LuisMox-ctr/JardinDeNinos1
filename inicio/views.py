from django.shortcuts import render
from .models import Reconocimiento

# Create your views here.

def principal(request):
    return render(request,"inicio/principal.html")
#ff
def tareas(request):
    return render(request,"inicio/tareas.html")

def dudas(request):
    return render(request,"inicio/dudas.html")

def reconocimientos(request):
    return render(request,"inicio/reconocimientos.html")


