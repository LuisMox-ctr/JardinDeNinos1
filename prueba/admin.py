from django.contrib import admin
from .models import Reconocimiento
# Register your models here.

@admin.register(Reconocimiento)
class ReconocimientoAdmin(admin.ModelAdmin):
    
    list_display = ('titulo', 'usuario', 'fecha_otorgado')
    list_filter = ('usuario', 'fecha_otorgado')
    search_fields = ('titulo', 'descripcion')