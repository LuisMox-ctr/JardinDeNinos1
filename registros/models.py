from django.db import models

# Create your models here.
#<Luis alejandro Zacarias gonzalez
class Alumnos(models.Model):

    ident = models.CharField(max_length=12, verbose_name="Identificacion")
    nombre = models.TextField(verbose_name="Nombre") 
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado") 
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Actualizado")

    class Meta:
        verbose_name="Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ["-created"]
    def __str__(self):
        return self.nombre

class Tareas(models.Model):
    idtarea = models.CharField(max_length=10, verbose_name="Numero de tarea")
    nombre = models.TextField(verbose_name="Nombre")
    descripcion= models.TextField(verbose_name="Descripcion")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado") 
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Actualizado")
    class Meta:
        verbose_name="Tarea"
        verbose_name_plural="Tareas"
        ordering=["-created"]
    def __str__(self):
        return self.nombre