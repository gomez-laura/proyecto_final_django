from django.shortcuts import render, redirect, get_object_or_404
from .models import Profesor
from .forms import ProfesorForm


def listarProfesores(request):
    profesores = Profesor.objects.all()
    return render(
        request,
        'profesor/profesores_lista.html',
        {'profesores': profesores}
    )


def detalleProfesor(request, pk):
    profesor = get_object_or_404(
        Profesor,
        pk=pk
    )
    return render(
        request,
        'profesor/profesor_detail.html',
        {'profesor': profesor}
    )


def crearProfesor(request):
    if request.method == "POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profesores:lista")
    else:
        form = ProfesorForm()
    return render(
        request,
        'profesor/profesor_form.html',
        {
            'form': form,
            'modo': 'crear'
        }
    )


def editarProfesor(request, pk):
    profesor = get_object_or_404(
        Profesor,
        pk=pk
    )
    if request.method == "POST":
        form = ProfesorForm(
            request.POST,
            instance=profesor
        )
        if form.is_valid():
            form.save()
            return redirect(
                "profesor:detalle",
                pk=profesor.pk
            )
    else:
        form = ProfesorForm(instance=profesor)
    return render(
        request,
        'profesor/profesor_form.html',
        {
            'form': form,
            'modo': 'editar',
            'profesor': profesor
        }
    )


def borrarProfesor(request, pk):
    profesor = get_object_or_404(
        Profesor,
        pk=pk
    )
    if request.method == "POST":
        profesor.delete()
        return redirect("profesores:lista")
    return render(
        request,
        'profesor/profesor_confirm_delete.html',
        {'profesor': profesor}
    )
