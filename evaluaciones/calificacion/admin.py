from django.contrib import admin
from .models import alumno


@admin.register(calificacion)
# Register your models here.
class CalificacionAdmin(admin.ModelAdmin):
    list_display = (
        'codigo',
        'alumno',
        'evaluacion',
        'nota'
    )

    search_fields = (
        'codigo',
        'alumno__nombre'
    )

    list_filter = (
        'evaluacion',
    )
