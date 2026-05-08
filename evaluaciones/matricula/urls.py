from django.urls import path

from .views import *

urlpatterns = [

    path('', MatriculaListView.as_view(),
         name='lista_matriculas'),

    path('<int:pk>/',
         MatriculaDetailView.as_view(),
         name='detalle_matricula'),

    path('nuevo/',
         MatriculaCreateView.as_view(),
         name='crear_matricula'),

    path('editar/<int:pk>/',
         MatriculaUpdateView.as_view(),
         name='editar_matricula'),

    path('eliminar/<int:pk>/',
         MatriculaDeleteView.as_view(),
         name='eliminar_matricula'),
]
