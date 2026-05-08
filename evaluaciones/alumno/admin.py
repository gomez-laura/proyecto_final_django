from django.contrib import admin
from .models import alumno


@admin.register(alumno)
# Register your models here.
class AlumnoAdmin(admin.ModelAdmin):
    list_display = (
        'dni',
        'nombre',
        'apellidos',
        'email',
        'telefono',
        'curso'
    )

    search_fields = (
        'dni',
        'nombre',
        'apellidos'
    )

    list_filter = ('curso',)
