from django.db import models

# Create your models here.
from alumno.models import Alumno
from evaluacion.models import Evaluacion

class Calificacion(models.Model):

    codigo = models.CharField(max_length=20, unique=True)

    alumno = models.ForeignKey(
        Alumno,
        on_delete=models.CASCADE,
        related_name='calificaciones'
    )

    evaluacion = models.ForeignKey(
        Evaluacion,
        on_delete=models.CASCADE,
        related_name='calificaciones'
    )

    nota = models.DecimalField(
        max_digits=4,
        decimal_places=2
    )

    observaciones = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        unique_together = ('alumno', 'evaluacion')

    def clean(self):

        if self.nota < 0 or self.nota > 10:
            raise ValidationError(
                "La nota debe estar entre 0 y 10"
            )

    def __str__(self):
        return f"{self.alumno} - {self.nota}"