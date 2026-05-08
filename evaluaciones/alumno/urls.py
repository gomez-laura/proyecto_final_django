from django.urls import path

from .views import *

urlpatterns = [

    path('', AlumnoListView.as_view(),
         name='lista_alumnos'),

    path('<int:pk>/',
         AlumnoDetailView.as_view(),
         name='detalle_alumno'),

    path('nuevo/',
         AlumnoCreateView.as_view(),
         name='crear_alumno'),

    path('editar/<int:pk>/',
         AlumnoUpdateView.as_view(),
         name='editar_alumno'),

    path('eliminar/<int:pk>/',
         AlumnoDeleteView.as_view(),
         name='eliminar_alumno'),
]
