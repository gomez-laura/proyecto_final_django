from django.contrib import admin
from .models import alumno


@admin.register(evaluacion)
# Register your models here.
class EvaluacionAdmin(admin.ModelAdmin):
    list_display = (
        'codigo',
        'titulo',
        'fecha',
        'tipo',
        'asignatura',
        'ponderacion'
    )

    search_fields = (
        'codigo',
        'titulo'
    )

    list_filter = (
        'tipo',
        'asignatura'
    )
