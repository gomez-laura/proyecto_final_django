from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from .models import Alumno

from .forms import AlumnoForm


def listarAlumnos(request):

    alumnos = Alumno.objects.all()

    return render(
        request,
        'alumnos/alumno.html',
        {'alumnos': alumnos}
    )


def detalleAlumno(request, pk):

    alumno = get_object_or_404(
        Alumno,
        pk=pk
    )

    return render(
        request,
        'alumnos/alumno_detail.html',
        {'alumno': alumno}
    )


def crearAlumno(request):

    if request.method == "POST":

        form = AlumnoForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("alumnos:lista")

    else:

        form = AlumnoForm()

    return render(
        request,
        'alumnos/alumno_form.html',
        {
            'form': form,
            'modo': 'crear'
        }
    )


def editarAlumno(request, pk):

    alumno = get_object_or_404(
        Alumno,
        pk=pk
    )

    if request.method == "POST":

        form = AlumnoForm(
            request.POST,
            instance=alumno
        )

        if form.is_valid():

            form.save()

            return redirect(
                "alumnos:detalle",
                pk=alumno.pk
            )

    else:

        form = AlumnoForm(instance=alumno)

    return render(
        request,
        'alumnos/alumno_form.html',
        {
            'form': form,
            'modo': 'editar',
            'alumno': alumno
        }
    )


def borrarAlumno(request, pk):

    alumno = get_object_or_404(
        Alumno,
        pk=pk
    )

    if request.method == "POST":

        alumno.delete()

        return redirect("alumnos:lista")

    return render(
        request,
        'alumnos/alumno_confirm_delete.html',
        {'alumno': alumno}
    )