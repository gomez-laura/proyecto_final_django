from rest_framework import serializers
from .models import Asignatura


class AsignaturaSerializer(serializers.ModelSerializer):
    #asignada_a = serializers.StringRelatedField()


    class Meta:
        model = Asignatura
        fields = [
            'codigo',
            'nombre',
            'descripcion',
            'profesor',
        ]
