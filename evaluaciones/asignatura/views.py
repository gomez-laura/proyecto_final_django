from django.shortcuts import render, redirect, get_object_or_404
from .models import Asignatura
from .forms import AsignaturaForm


def listarAsignaturas(request):
    asignaturas = Asignatura.objects.all()
    return render(
        request,
        'asignatura/asignaturas_lista.html',
        {'asignaturas': asignaturas}
    )


def detalleAsignatura(request, pk):
    asignatura = get_object_or_404(
        Asignatura,
        pk=pk
    )
    return render(
        request,
        'asignatura/asignatura_detail.html',
        {'asignatura': asignatura}
    )


def crearAsignatura(request):
    if request.method == "POST":
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("asignaturas:lista")
    else:
        form = AsignaturaForm()
    return render(
        request,
        'asignatura/asignatura_form.html',
        {
            'form': form,
            'modo': 'crear'
        }
    )


def editarAsignatura(request, pk):
    asignatura = get_object_or_404(
        Asignatura,
        pk=pk
    )
    if request.method == "POST":
        form = AsignaturaForm(
            request.POST,
            instance=asignatura
        )
        if form.is_valid():
            form.save()
            return redirect(
                "asignatura:detalle",
                pk=asignatura.pk
            )
    else:
        form = AsignaturaForm(instance=asignatura)
    return render(
        request,
        'asignatura/asignatura_form.html',
        {
            'form': form,
            'modo': 'editar',
            'asignatura': asignatura
        }
    )


def borrarAsignatura(request, pk):
    asignatura = get_object_or_404(
        Asignatura,
        pk=pk
    )
    if request.method == "POST":
        asignatura.delete()
        return redirect("asignatura:lista")
    return render(
        request,
        'asignatura/asignatura_confirm_delete.html',
        {'asignatura': asignatura}
    )
