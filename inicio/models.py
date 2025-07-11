from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#aaa

class Reconocimiento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reconocimientos')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='reconocimientos/')
    fecha_otorgado = models.DateField()
    
    def __str__(self):
        return f"{self.titulo} - {self.usuario.username}"