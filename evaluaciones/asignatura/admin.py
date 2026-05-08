from django.contrib import admin
from .models import alumno


@admin.register(asignatura)
# Register your models here.
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = (
        'codigo',
        'nombre',
        'profesor'
    )

    search_fields = (
        'codigo',
        'nombre'
    )

    list_filter = ('profesor',)
