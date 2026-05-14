from django.urls import path
from . import views

app_name = "asignatura"

urlpatterns = [

    path(
        "",
        views.listarAsignaturas,
        name="lista"
    ),

    path(
        "nuevo/",
        views.crearAsignatura,
        name="crear"
    ),

    path(
        "<int:pk>/",
        views.detalleAsignatura,
        name="detalle"
    ),

    path(
        "<int:pk>/editar/",
        views.editarAsignatura,
        name="editar"
    ),

    path(
        "<int:pk>/borrar/",
        views.borrarAsignatura,
        name="borrar"
    ),
]