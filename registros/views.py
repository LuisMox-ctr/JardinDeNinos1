from django.shortcuts import render
from .models import Alumnos, Tareas, AlumnoTarea
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from .forms import EntregarTareaForm
from django.db.models import Q

from .models import Duda
from .forms import DudaForm

# Create your views here.
def registros(request):
    # Si llega un filtro por GET, lo usamos
    filtro_estado = request.GET.get("estado", "todas")
    alumno_id = request.GET.get("alumno","")
    q = request.GET.get("q", "").strip()
    
    asignaciones = (AlumnoTarea.objects
        .select_related('alumno', 'tarea')
        .all())

    # Filtro por estado
    if filtro_estado in ("pendiente","terminada"):
        asignaciones = asignaciones.filter(estado=filtro_estado)
        # Filtro por alumno (id exacto)
    if alumno_id:
        asignaciones = asignaciones.filter(alumno_id=alumno_id)
         # Búsqueda libre (nombre o ident)
    if q:
        asignaciones = asignaciones.filter(
            Q(alumno__nombre__icontains=q) | 
            Q(tarea__nombre__icontains=q)
        )
    '''if filtro_estado == "pendiente":
        asignaciones = AlumnoTarea.objects.filter(estado="pendiente")
    elif filtro_estado == "terminada":
        asignaciones = AlumnoTarea.objects.filter(estado="terminada")
    else:
        asignaciones = AlumnoTarea.objects.all()'''

    alumnos_con_tareas = {}
    for asig in asignaciones.order_by('alumno__nombre'):
        aid = asig.alumno.id
        if aid not in alumnos_con_tareas:
            alumnos_con_tareas[aid] = {
                'alumno': asig.alumno,
                'tareas': []
            }
        alumnos_con_tareas[aid]['tareas'].append(asig)
        
        alumnos_list= Alumnos.objects.all().order_by('nombre')
        return render(request, "registros/principal.html", {
        "alumnos_con_tareas": alumnos_con_tareas,
        "filtro_estado": filtro_estado,
        "alumnos_list": alumnos_list,
        "alumno_seleccionado": alumno_id,
        "q": q,
    })
    '''alumnos_con_tareas = {}
    for asignacion in asignaciones:
        alumno_id = asignacion.alumno.id
        if alumno_id not in alumnos_con_tareas:
            alumnos_con_tareas[alumno_id] = {
                'alumno': asignacion.alumno,
                'tareas': []
            }
        alumnos_con_tareas[alumno_id]['tareas'].append(asignacion)
    
    return render(request, "registros/principal.html", {
        "alumnos_con_tareas": alumnos_con_tareas,
        "filtro_estado": filtro_estado
    })'''

def entregar_tarea(request, tarea_id):
    asignacion = get_object_or_404(AlumnoTarea, id=tarea_id)

    if request.method == 'POST':
        form = EntregarTareaForm(request.POST, request.FILES, instance=asignacion)
        if form.is_valid():
            asignacion = form.save(commit=False)
            asignacion.estado = 'terminada'
            asignacion.fecha_terminada = timezone.now()
            asignacion.save()
            messages.success(request, "¡Tarea entregada correctamente!")
            return redirect('tareas')  
    else:
        form = EntregarTareaForm(instance=asignacion)

    return render(request, "registros/entregar_tarea.html", {"form": form, "asignacion": asignacion})


def dudas(request):
    if request.method == "POST":
        form = DudaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dudas')  # redirige para limpiar el form
    else:
        form = DudaForm()

    dudas_list = Duda.objects.order_by('-created')

    return render(request, "registros/dudas.html", {
        'form': form,
        'dudas': dudas_list,
    })