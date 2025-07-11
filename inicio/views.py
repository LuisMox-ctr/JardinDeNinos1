from django.shortcuts import render


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


def reconocimientos_view(request):
    reconocimientos_del_usuario = Reconocimiento.objects.filter(usuario=request.user).order_by('-fecha_otorgado')
    
    contexto = {
        'reconocimientos': reconocimientos_del_usuario
    }
    
    return render(request, 'inicio/reconocimientos.html', contexto)