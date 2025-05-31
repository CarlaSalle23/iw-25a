from django.db import models

class Silabo(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    curso = models.CharField(max_length=100)
    docente = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.curso}"
