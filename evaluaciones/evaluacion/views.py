from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import *

from .models import Evaluacion


class EvaluacionListView(ListView):
    model = Evaluacion
    template_name = 'evaluaciones/lista.html'


class EvaluacionDetailView(DetailView):
    model = Evaluacion
    template_name = 'evaluaciones/detalle.html'


class EvaluacionCreateView(CreateView):
    model = Evaluacion
    fields = '__all__'

    template_name = 'evaluaciones/formulario.html'

    success_url = reverse_lazy('lista_evaluaciones')


class EvaluacionUpdateView(UpdateView):
    model = Evaluacion
    fields = '__all__'

    template_name = 'evaluaciones/formulario.html'

    success_url = reverse_lazy('lista_evaluaciones')


class EvaluacionDeleteView(DeleteView):
    model = Evaluacion

    template_name = 'evaluaciones/eliminar.html'

    success_url = reverse_lazy('lista_evaluaciones')
