from django.contrib import admin
from .models import Alumnos
from .models import Tareas
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