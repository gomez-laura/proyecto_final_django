from django.urls import path

from . import views

app_name = "alumnos"

urlpatterns = [

    path(
        "",
        views.listarAlumnos,
        name="lista"
    ),

    path(
        "nuevo/",
        views.crearAlumno,
        name="crear"
    ),

    path(
        "<int:pk>/",
        views.detalleAlumno,
        name="detalle"
    ),

    path(
        "<int:pk>/editar/",
        views.editarAlumno,
        name="editar"
    ),

    path(
        "<int:pk>/borrar/",
        views.borrarAlumno,
        name="borrar"
    ),
]