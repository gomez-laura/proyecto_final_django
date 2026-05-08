from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import *

from .models import Calificacion


class CalificacionListView(ListView):
    model = Calificacion
    template_name = 'calificaciones/lista.html'


class CalificacionDetailView(DetailView):
    model = Calificacion
    template_name = 'calificaciones/detalle.html'


class CalificacionCreateView(CreateView):
    model = Calificacion
    fields = '__all__'

    template_name = 'calificaciones/formulario.html'

    success_url = reverse_lazy('lista_calificaciones')


class CalificacionUpdateView(UpdateView):
    model = Calificacion
    fields = '__all__'

    template_name = 'calificaciones/formulario.html'

    success_url = reverse_lazy('lista_calificaciones')


class CalificacionDeleteView(DeleteView):
    model = Calificacion

    template_name = 'calificaciones/eliminar.html'

    success_url = reverse_lazy('lista_calificaciones')
