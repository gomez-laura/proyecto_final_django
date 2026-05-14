from django.urls import path
from . import views

app_name = "evaluacion"

urlpatterns = [

    path(
        "",
        views.listarEvaluaciones,
        name="lista"
    ),

    path(
        "nuevo/",
        views.crearEvaluacion,
        name="crear"
    ),

    path(
        "<int:pk>/",
        views.detalleEvaluacion,
        name="detalle"
    ),

    path(
        "<int:pk>/editar/",
        views.editarEvaluacion,
        name="editar"
    ),

    path(
        "<int:pk>/borrar/",
        views.borrarEvaluacion,
        name="borrar"
    ),
]