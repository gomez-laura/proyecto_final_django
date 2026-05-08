from django.urls import path

from .views import *

urlpatterns = [

    path('', ProfesorListView.as_view(),
         name='lista_profesores'),

    path('<int:pk>/',
         ProfesorDetailView.as_view(),
         name='detalle_profesor'),

    path('nuevo/',
         ProfesorCreateView.as_view(),
         name='crear_profesor'),

    path('editar/<int:pk>/',
         ProfesorUpdateView.as_view(),
         name='editar_profesor'),

    path('eliminar/<int:pk>/',
         ProfesorDeleteView.as_view(),
         name='eliminar_profesor'),
]
