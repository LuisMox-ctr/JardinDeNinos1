from django.shortcuts import render

#


#Luis humberto
def principal(request):
    return render(request, "inicio/principal.html")
#brandon vargas
def tareas(request):
    return render(request, "inicio/tareas.html")
#Diego daniel
def dudas(request):
    return render(request, "inicio/dudas.html")
#Luis humberto
def reconocimientos(request):
    return render(request, "inicio/reconocimientos.html")



#prueba