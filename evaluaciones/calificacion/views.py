from django.shortcuts import render, redirect, get_object_or_404
from .models import Calificacion
from .forms import CalificacionForm


def listarCalificaciones(request):
    calificaciones = Calificacion.objects.all()
    return render(
        request,
        'calificacion/calificaciones_lista.html',
        {'calificaciones': calificaciones}
    )


def detalleCalificacion(request, pk):
    calificacion = get_object_or_404(
        Calificacion,
        pk=pk
    )
    return render(
        request,
        'calificacion/calificacion_detail.html',
        {'calificacion': calificacion}
    )


def crearCalificacion(request):
    if request.method == "POST":
        form = CalificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("calificaciones:lista")
    else:
        form = CalificacionForm()
    return render(
        request,
        'calificacion/calificacion_form.html',
        {
            'form': form,
            'modo': 'crear'
        }
    )


def editarCalificacion(request, pk):
    calificacion = get_object_or_404(
        Calificacion,
        pk=pk
    )
    if request.method == "POST":
        form = CalificacionForm(
            request.POST,
            instance=calificacion
        )
        if form.is_valid():
            form.save()
            return redirect(
                "calificacion:detalle",
                pk=calificacion.pk
            )
    else:
        form = CalificacionForm(instance=calificacion)
    return render(
        request,
        'calificacion/calificacion_form.html',
        {
            'form': form,
            'modo': 'editar',
            'calificacion': calificacion
        }
    )


def borrarCalificacion(request, pk):
    calificacion = get_object_or_404(
        Calificacion,
        pk=pk
    )
    if request.method == "POST":
        calificacion.delete()
        return redirect("calificaciones:lista")
    return render(
        request,
        'calificacion/calificacion_confirm_delete.html',
        {'calificacion': calificacion}
    )
