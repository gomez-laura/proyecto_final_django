from django.db.models import Avg

media = Calificacion.objects.filter(
    alumno=alumno
).aggregate(
    Avg('nota')
)