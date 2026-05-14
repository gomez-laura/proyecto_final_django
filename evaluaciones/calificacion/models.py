from django.db import models

from alumno.models import Alumno
from evaluacion.models import Evaluacion


class Calificacion(models.Model):

    codigo = models.CharField(max_length=20)

    alumno = models.ForeignKey(
        Alumno,
        on_delete=models.CASCADE
    )

    evaluacion = models.ForeignKey(
        Evaluacion,
        on_delete=models.CASCADE
    )

    nota = models.DecimalField(
        max_digits=4,
        decimal_places=2
    )

    observaciones = models.TextField()

    def __str__(self):

        return f"{self.alumno} - {self.nota}"