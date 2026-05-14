from django.shortcuts import render, redirect, get_object_or_404
from .models import Evaluacion
from .forms import EvaluacionForm


def listarEvaluaciones(request):
    evaluaciones = Evaluacion.objects.all()
    return render(
        request,
        'evaluacion/evaluaciones_lista.html',
        {'evaluaciones': evaluaciones}
    )


def detalleEvaluacion(request, pk):
    evaluacion = get_object_or_404(
        Evaluacion,
        pk=pk
    )
    return render(
        request,
        'evaluacion/evaluacion_detail.html',
        {'evaluacion': evaluacion}
    )


def crearEvaluacion(request):
    if request.method == "POST":
        form = EvaluacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("evaluaciones:lista")
    else:
        form = EvaluacionForm()
    return render(
        request,
        'evaluacion/evaluacion_form.html',
        {
            'form': form,
            'modo': 'crear'
        }
    )


def editarEvaluacion(request, pk):
    evaluacion = get_object_or_404(
        Evaluacion,
        pk=pk
    )
    if request.method == "POST":
        form = EvaluacionForm(
            request.POST,
            instance=evaluacion
        )
        if form.is_valid():
            form.save()
            return redirect(
                "evaluacion:detalle",
                pk=evaluacion.pk
            )
    else:
        form = EvaluacionForm(instance=evaluacion)
    return render(
        request,
        'evaluacion/evaluacion_form.html',
        {
            'form': form,
            'modo': 'editar',
            'evaluacion': evaluacion
        }
    )


def borrarEvaluacion(request, pk):
    evaluacion = get_object_or_404(
        Evaluacion,
        pk=pk
    )
    if request.method == "POST":
        evaluacion.delete()
        return redirect("evaluaciones:lista")
    return render(
        request,
        'evaluacion/evaluacion_confirm_delete.html',
        {'evaluacion': evaluacion}
    )
