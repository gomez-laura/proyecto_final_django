from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Alumno


class AlumnoListView(ListView):
    model = Alumno
    template_name = 'alumnos/lista.html'
    context_object_name = 'alumnos'


class AlumnoDetailView(DetailView):
    model = Alumno
    template_name = 'alumnos/detalle.html'


class AlumnoCreateView(CreateView):
    model = Alumno
    fields = '__all__'
    template_name = 'alumnos/formulario.html'

    success_url = reverse_lazy('lista_alumnos')


class AlumnoUpdateView(UpdateView):
    model = Alumno
    fields = '__all__'
    template_name = 'alumnos/formulario.html'

    success_url = reverse_lazy('lista_alumnos')


class AlumnoDeleteView(DeleteView):
    model = Alumno
    template_name = 'alumnos/eliminar.html'

    success_url = reverse_lazy('lista_alumnos')
