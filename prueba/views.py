from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Reconocimiento


# Create your views here.

def reconocimientos_view(request):
    # Filtra los reconocimientos para mostrar solo los del usuario logueado.
    reconocimientos_del_usuario = Reconocimiento.objects.filter(usuario=request.user).order_by('-fecha_otorgado')
    
    contexto = {
        'reconocimientos': reconocimientos_del_usuario
    }
    
    return render(request, 'prueba/reconocimientos.html', contexto)