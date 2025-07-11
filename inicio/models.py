from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Alumnos(models.Model):  # define la estructura de nuestra tabla
    nombre = models.Charfield(max_length=12)  
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografia")
    grado = models.Charfield(max_length=10)
    grupo = models.Charfield(max_length=10)
    created = models.DateTimeField(auto_now_add=True)  # Fecha y Hora
    updated = models.DateTimeField(auto_now=True)  # Se actualiza al guardar cambios

#aaa

class Reconocimiento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reconocimientos')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='reconocimientos/')
    fecha_otorgado = models.DateField()
    
    def __str__(self):
        return f"{self.titulo} - {self.usuario.username}"

