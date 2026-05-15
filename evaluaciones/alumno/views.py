from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view #se añade esta línea
from rest_framework.response import Response
from .serializer import AlumnoSerializer # Importa tu serializador
from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumno
from .forms import AlumnoForm


def listarAlumnos(request):
    alumnos = Alumno.objects.all()
    return render(
        request,
        'alumno/alumnos_lista.html',
        {'alumnos': alumnos}
    )


def detalleAlumno(request, pk):
    alumno = get_object_or_404(
        Alumno,
        pk=pk
    )
    return render(
        request,
        'alumno/alumno_detail.html',
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
        'alumno/alumno_form.html',
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
                "alumno:detalle",
                pk=alumno.pk
            )
    else:
        form = AlumnoForm(instance=alumno)
    return render(
        request,
        'alumno/alumno_form.html',
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
        'alumno/alumno_confirm_delete.html',
        {'alumno': alumno}
    )


@api_view(['GET']) #se añade este metodo

def api_lista_alumnos(request):
    alumnos = Alumno.objects.all()
    serializer = AlumnoSerializer(alumnos, many=True)
    return Response(serializer.data)
