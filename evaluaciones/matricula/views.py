from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import *

from .models import Matricula


class MatriculaListView(ListView):
    model = Matricula
    template_name = 'matriculas/lista.html'


class MatriculaDetailView(DetailView):
    model = Matricula
    template_name = 'matriculas/detalle.html'


class MatriculaCreateView(CreateView):
    model = Matricula
    fields = '__all__'

    template_name = 'matriculas/formulario.html'

    success_url = reverse_lazy('lista_matriculas')


class MatriculaUpdateView(UpdateView):
    model = Matricula
    fields = '__all__'

    template_name = 'matriculas/formulario.html'

    success_url = reverse_lazy('lista_matriculas')


class MatriculaDeleteView(DeleteView):
    model = Matricula

    template_name = 'matriculas/eliminar.html'

    success_url = reverse_lazy('lista_matriculas')
