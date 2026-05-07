from django.db import models

# Create your models here.
from asignatura.models import Asignatura

class Evaluacion(models.Model):

    TIPOS = [
        ('EXAMEN', 'Examen'),
        ('PRACTICA', 'Práctica'),
        ('TRABAJO', 'Trabajo'),
    ]

    codigo = models.CharField(max_length=20, unique=True)
    titulo = models.CharField(max_length=100)
    fecha = models.DateField()

    tipo = models.CharField(
        max_length=20,
        choices=TIPOS
    )

    asignatura = models.ForeignKey(
        Asignatura,
        on_delete=models.CASCADE,
        related_name='evaluaciones'
    )

    ponderacion = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    def __str__(self):
        return self.titulo