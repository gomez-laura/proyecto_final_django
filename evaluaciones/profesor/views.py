from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import *

from .models import Profesor


class ProfesorListView(ListView):
    model = Profesor
    template_name = 'profesores/lista.html'


class ProfesorDetailView(DetailView):
    model = Profesor
    template_name = 'profesores/detalle.html'


class ProfesorCreateView(CreateView):
    model = Profesor
    fields = '__all__'

    template_name = 'profesores/formulario.html'

    success_url = reverse_lazy('lista_profesores')


class ProfesorUpdateView(UpdateView):
    model = Profesor
    fields = '__all__'

    template_name = 'profesores/formulario.html'

    success_url = reverse_lazy('lista_profesores')


class ProfesorDeleteView(DeleteView):
    model = Profesor

    template_name = 'profesores/eliminar.html'

    success_url = reverse_lazy('lista_profesores')
