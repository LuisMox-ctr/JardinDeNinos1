from django.contrib import admin
from .models import Alumnos
from .models import Alumnos, Tareas, Maestros, AlumnoTarea, Duda, Reconocimiento
# Register your models here.
#<Luis alejandro Zacarias gonzalez
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display = ("ident","nombre","created","updated")
    search_fields = ("ident","nombre")
    date_hierarchy = "created"

admin.site.register(Alumnos, AdministrarModelo)

class AdministrarTareas(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display = ("descripcion","created","updated")
    search_fields = ("descripcion","nombre")
    date_hierarchy = "created"

admin.site.register(Tareas, AdministrarTareas)

class AdministrarAlumnoTarea(admin.ModelAdmin):
    list_display = ("alumno", "tarea", "estado", "fecha_asignada")
    list_filter = ("estado", "fecha_asignada")
    search_fields = ("alumno__nombre", "tarea__nombre")
    date_hierarchy = "fecha_asignada"
    readonly_fields = ('fecha_asignada',)

admin.site.register(AlumnoTarea, AdministrarAlumnoTarea)


class AdministrarDudas(admin.ModelAdmin):
    list_display = ("asunto", "created")
    search_fields = ("asunto", "descripcion")
    date_hierarchy = "created"
    readonly_fields = ('created',)
    
admin.site.register(Duda, AdministrarDudas)

class ReconocimientoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "alumno", "maestro", "created")
    list_filter = ("maestro", "alumno")
    search_fields = ("titulo", "motivo")
    
admin.site.register(Reconocimiento, ReconocimientoAdmin)

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    
admin.site.register(Maestros, ProfesorAdmin)