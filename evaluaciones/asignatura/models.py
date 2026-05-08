from django.db import models
from profesor.models import Profesor


# Create your models here.

class Asignatura(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    profesor = models.ForeignKey(
        Profesor,
        on_delete=models.CASCADE,
        related_name='asignaturas'
    )

    def _str_(self):
        return self.nombre
