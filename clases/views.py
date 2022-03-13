from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from clases.models import Curso
import random

# Create your views here.

def nuevos_cursos(request):
    
    camada = random.randrange(999, 5000)
    c = Curso(nombre = "Python Course", camada=camada)
    c.save()
    return HttpResponse(f"Se creo el curso: {c.nombre} camada número: {c.camada}")
    