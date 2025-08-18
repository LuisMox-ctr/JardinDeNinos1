from django.db import models

# Create your models here.
#<Luis alejandro Zacarias gonzalez
class Alumnos(models.Model):
    ident = models.CharField(max_length=12, verbose_name="Identificacion")
    nombre = models.TextField(verbose_name="Nombre")
    tarea = models.ForeignKey('Tareas', on_delete=models.CASCADE, verbose_name="Tarea", null=True, blank=True)  # Agregué null=True, blank=True
    foto = models.ImageField(upload_to='alumnos/', verbose_name="Foto", null=True, blank=True)  # Agregué el campo foto
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado") 
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")  # Cambié auto_now_add por auto_now

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

class Maestros(models.Model):
    ident = models.CharField(max_length=12, verbose_name="Identificacion")
    nombre = models.TextField(verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = "Maestro"
        verbose_name_plural = "Maestros"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre
    
    
class AlumnoTarea(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('terminada', 'Terminada'),
    ]
    
    alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE, verbose_name="Alumno")
    tarea = models.ForeignKey(Tareas, on_delete=models.CASCADE, verbose_name="Tarea")
    estado = models.CharField(max_length=10, choices=ESTADOS, default='pendiente', verbose_name="Estado")
    fecha_asignada = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Asignada")
    fecha_terminada = models.DateTimeField(null=True, blank=True, verbose_name="Fecha Terminada")
    evidencia = models.FileField(upload_to='evidencias/', null=True, blank=True, verbose_name="Evidencia")

    
    class Meta:
        verbose_name = "Asignación de Tarea"
        verbose_name_plural = "Asignaciones de Tareas"
        unique_together = ['alumno', 'tarea']  # Un alumno no puede tener la misma tarea dos veces
        ordering = ["-fecha_asignada"]
    
    def __str__(self):
        return f"{self.alumno.nombre} - {self.tarea.nombre} ({self.estado})"
   
   
class Duda(models.Model):
     asunto = models.CharField(max_length=200)
     descripcion = models.TextField()
     respuesta = models.TextField(blank=True, null=True)  # el maestro/admin puede responder
     created = models.DateTimeField(auto_now_add=True)

     def __str__(self):
        return self.asunto
    
    
class Reconocimiento(models.Model):
    titulo = models.CharField(max_length=100, help_text="Ej: Estrella de asistencia")
    motivo = models.TextField()
    imagen = models.ImageField(upload_to="reconocimientos/")  # se guardarán en media/reconocimientos/
    alumno = models.ForeignKey(Alumnos, on_delete=models.CASCADE, related_name="reconocimientos")
    maestro = models.ForeignKey(Maestros, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.alumno.nombre}"