from django.shortcuts import render
from .models import Alumnos, Tareas, AlumnoTarea

# Create your views here.
def registros(request):
    asignaciones_pendientes = AlumnoTarea.objects.filter(estado='pendiente')
    
    alumnos_con_tareas = {}
    for asignacion in asignaciones_pendientes:
        alumno_id = asignacion.alumno.id
        if alumno_id not in alumnos_con_tareas:
            alumnos_con_tareas[alumno_id] = {
                'alumno': asignacion.alumno,
                'tareas_pendientes': []
            }
        alumnos_con_tareas[alumno_id]['tareas_pendientes'].append(asignacion)
    
    return render(request, "registros/principal.html", {"alumnos_con_tareas": alumnos_con_tareas})