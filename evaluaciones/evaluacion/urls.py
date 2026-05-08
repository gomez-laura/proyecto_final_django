from django.urls import path

from .views import *

urlpatterns = [

    path('', EvaluacionListView.as_view(),
         name='lista_evaluaciones'),

    path('<int:pk>/',
         EvaluacionDetailView.as_view(),
         name='detalle_evaluacion'),

    path('nuevo/',
         EvaluacionCreateView.as_view(),
         name='crear_evaluacion'),

    path('editar/<int:pk>/',
         EvaluacionUpdateView.as_view(),
         name='editar_evaluacion'),

    path('eliminar/<int:pk>/',
         EvaluacionDeleteView.as_view(),
         name='eliminar_evaluacion'),
]
