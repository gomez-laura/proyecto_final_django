from django.contrib import admin
from .models import matricula


@admin.register(matricula)
# Register your models here.
class MatriculaAdmin(admin.ModelAdmin):
    list_display = (
        'alumno',
        'asignatura',
        'curso_academico',
        'fecha_matricula',
        'estado'
    )

    search_fields = (
        'alumno__nombre',
        'asignatura__nombre'
    )

    list_filter = (
        'curso_academico',
        'estado'
    )
