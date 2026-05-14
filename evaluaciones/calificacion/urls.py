from django.urls import path
from . import views

app_name = "calificacion"

urlpatterns = [

    path(
        "",
        views.listarCalificaciones,
        name="lista"
    ),

    path(
        "nuevo/",
        views.crearCalificacion,
        name="crear"
    ),

    path(
        "<int:pk>/",
        views.detalleCalificacion,
        name="detalle"
    ),

    path(
        "<int:pk>/editar/",
        views.editarCalificacion,
        name="editar"
    ),

    path(
        "<int:pk>/borrar/",
        views.borrarCalificacion,
        name="borrar"
    ),
]