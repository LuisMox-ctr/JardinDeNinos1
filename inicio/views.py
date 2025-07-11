from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Vistas que ya tenías
def principal(request):
    return render(request, "inicio/principal.html")

def tareas(request):
    return render(request, "inicio/tareas.html")

def dudas(request):
    return render(request, "inicio/dudas.html")

