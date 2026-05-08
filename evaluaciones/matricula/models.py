from django.db import models
from alumno.models import Alumno
from asignatura.models import Asignatura


# Create your models here.


class Matricula(models.Model):
    alumno = models.ForeignKey(
        Alumno,
        on_delete=models.CASCADE
    )

    asignatura = models.ForeignKey(
        Asignatura,
        on_delete=models.CASCADE
    )

    curso_academico = models.CharField(max_length=20)

    fecha_matricula = models.DateField(auto_now_add=True)

    estado = models.CharField(
        max_length=20,
        default='ACTIVA'
    )

    class Meta:
        unique_together = ('alumno', 'asignatura')

    def __str__(self):
        return f"{self.alumno} -> {self.asignatura}"
