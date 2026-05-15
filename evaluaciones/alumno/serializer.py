from rest_framework import serializers
from .models import Alumno


class AlumnoSerializer(serializers.ModelSerializer):
    #asignada_a = serializers.StringRelatedField()


    class Meta:
        model = Alumno
        fields = [
            'dni',
            'nombre',
            'apellidos',
            'email',
            'telefono',
            'curso',
            #'asignada_a',
        ]
