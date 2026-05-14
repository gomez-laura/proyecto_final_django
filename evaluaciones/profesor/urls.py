from django.urls import path
from . import views

app_name = "profesor"

urlpatterns = [

    path(
        "",
        views.listarProfesores,
        name="lista"
    ),

    path(
        "nuevo/",
        views.crearProfesor,
        name="crear"
    ),

    path(
        "<int:pk>/",
        views.detalleProfesor,
        name="detalle"
    ),

    path(
        "<int:pk>/editar/",
        views.editarProfesor,
        name="editar"
    ),

    path(
        "<int:pk>/borrar/",
        views.borrarProfesor,
        name="borrar"
    ),
]