from django.urls import path

from .views import *

urlpatterns = [

    path('', CalificacionListView.as_view(),
         name='lista_calificaciones'),

    path('<int:pk>/',
         CalificacionDetailView.as_view(),
         name='detalle_calificacion'),

    path('nuevo/',
         CalificacionCreateView.as_view(),
         name='crear_calificacion'),

    path('editar/<int:pk>/',
         CalificacionUpdateView.as_view(),
         name='editar_calificacion'),

    path('eliminar/<int:pk>/',
         CalificacionDeleteView.as_view(),
         name='eliminar_calificacion'),
]
