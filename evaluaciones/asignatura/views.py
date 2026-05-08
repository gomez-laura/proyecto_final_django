from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import *

from .models import Asignatura


class AsignaturaListView(ListView):
    model = Asignatura
    template_name = 'asignaturas/lista.html'


class AsignaturaDetailView(DetailView):
    model = Asignatura
    template_name = 'asignaturas/detalle.html'


class AsignaturaCreateView(CreateView):
    model = Asignatura
    fields = '__all__'

    template_name = 'asignaturas/formulario.html'

    success_url = reverse_lazy('lista_asignaturas')


class AsignaturaUpdateView(UpdateView):
    model = Asignatura
    fields = '__all__'

    template_name = 'asignaturas/formulario.html'

    success_url = reverse_lazy('lista_asignaturas')


class AsignaturaDeleteView(DeleteView):
    model = Asignatura

    template_name = 'asignaturas/eliminar.html'

    success_url = reverse_lazy('lista_asignaturas')
