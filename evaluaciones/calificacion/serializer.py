from rest_framework import serializers
from .models import Calificacion


class CalificacionSerializer(serializers.ModelSerializer):
    #asignada_a = serializers.StringRelatedField()


    class Meta:
        model = Calificacion
        fields = [
            'codigo',
            'alumno',
            'apellidos',
            'email',
            'telefono',
            'curso',
            #'asignada_a',
        ]
