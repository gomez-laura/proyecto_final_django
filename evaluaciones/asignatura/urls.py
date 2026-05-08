from django.urls import path

from .views import *

urlpatterns = [

    path('', AsignaturaListView.as_view(),
         name='lista_asignaturas'),

    path('<int:pk>/',
         AsignaturaDetailView.as_view(),
         name='detalle_asignatura'),

    path('nuevo/',
         AsignaturaCreateView.as_view(),
         name='crear_asignatura'),

    path('editar/<int:pk>/',
         AsignaturaUpdateView.as_view(),
         name='editar_asignatura'),

    path('eliminar/<int:pk>/',
         AsignaturaDeleteView.as_view(),
         name='eliminar_asignatura'),
]
