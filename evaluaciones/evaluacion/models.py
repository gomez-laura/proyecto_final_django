from django.db import models

from asignatura.models import Asignatura


class Evaluacion(models.Model):

    TIPOS = [

        ('EXAMEN', 'Examen'),

        ('TRABAJO', 'Trabajo'),

        ('PRACTICA', 'Practica'),
    ]

    codigo = models.CharField(max_length=20)

    titulo = models.CharField(max_length=100)

    fecha = models.DateField()

    tipo = models.CharField(
        max_length=20,
        choices=TIPOS
    )

    asignatura = models.ForeignKey(
        Asignatura,
        on_delete=models.CASCADE
    )

    ponderacion = models.DecimalField(
        max_digits=4,
        decimal_places=2
    )

    def __str__(self):

        return self.titulo