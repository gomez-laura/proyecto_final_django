from django.db import models

from alumnos.models import Alumno

from asignaturas.models import Asignatura

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

    estado = models.CharField(max_length=20)

    def __str__(self):

        return f"{self.alumno} - {self.asignatura}"