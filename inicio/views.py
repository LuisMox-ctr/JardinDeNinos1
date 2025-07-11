from django.shortcuts import render




def principal(request):
    return render(request, "inicio/principal.html")

def tareas(request):
    return render(request, "inicio/tareas.html")

def dudas(request):
    return render(request, "inicio/dudas.html")

def reconocimientos(request):
    return render(request, "inicio/reconocimientos.html")

#prueba