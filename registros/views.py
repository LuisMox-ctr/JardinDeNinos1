from django.shortcuts import render
from .models import Alumnos, Tareas, AlumnoTarea
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from .forms import EntregarTareaForm

# Create your views here.
def registros(request):
    # Si llega un filtro por GET, lo usamos
    filtro_estado = request.GET.get("estado", "todas")  

    if filtro_estado == "pendiente":
        asignaciones = AlumnoTarea.objects.filter(estado="pendiente")
    elif filtro_estado == "terminada":
        asignaciones = AlumnoTarea.objects.filter(estado="terminada")
    else:
        asignaciones = AlumnoTarea.objects.all()

    alumnos_con_tareas = {}
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
    })

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