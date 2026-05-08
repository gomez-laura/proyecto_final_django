from django.contrib import admin
from .models import profesor


@admin.register(profesor)
# Register your models here.
class ProfesorAdmin(admin.ModelAdmin):
    list_display = (
        'dni',
        'nombre',
        'apellidos',
        'email',
        'telefono',
        'departamento'
    )

    search_fields = (
        'dni',
        'nombre',
        'apellidos'
    )

    list_filter = ('departamento',)
