from django.db import models

from profesores.models import Profesor

class Asignatura(models.Model):

    codigo = models.CharField(max_length=20)

    nombre = models.CharField(max_length=100)

    descripcion = models.TextField()

    profesor = models.ForeignKey(
        Profesor,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    def __str__(self):

        return self.nombre