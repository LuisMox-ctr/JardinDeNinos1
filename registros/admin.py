from django.contrib import admin
from .models import Alumnos
from .models import Tareas
# Register your models here.
#<Luis alejandro Zacarias gonzalez
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Alumnos, AdministrarModelo)

class AdministrarTareas(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Tareas)