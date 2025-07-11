from django.contrib import admin
from .models import Reconocimiento
# Register your models here.

@admin.register(Reconocimiento)
class ReconocimientoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usuario', 'fecha_otorgado')
    list_filter = ('fecha_otorgado', 'usuario')
    search_fields = ('titulo', 'descripcion', 'usuario__username')