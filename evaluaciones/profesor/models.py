from django.db import models

class Profesor(models.Model):

    dni = models.CharField(max_length=9)

    nombre = models.CharField(max_length=100)

    apellidos = models.CharField(max_length=150)

    email = models.EmailField()

    telefono = models.CharField(max_length=20)

    departamento = models.CharField(max_length=100)

    def __str__(self):

        return f"{self.nombre} {self.apellidos}"