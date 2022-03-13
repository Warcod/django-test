import imp
from django.forms import DateField
from django.shortcuts import render
from .models import Hermano
from django.http import HttpResponse

# Create your views here.


def crear_hermanos(request):
    h1 = Hermano(nombre = 'Carla', edad = 34, fechaDeNacimiento = '1988-09-26')
    h2 = Hermano(nombre = 'Florencia', edad = 32, fechaDeNacimiento = '1990-01-26')
    h3 = Hermano(nombre = 'Guido', edad = 24, fechaDeNacimiento = '1998-01-09')
    
    h1.save()
    h2.save()
    h3.save()    
    
    return HttpResponse(f"""Los tres hermanos de la familia son:
                        {h1.nombre}, que tiene {h1.edad} años y su nacimiento fue en {h1.fechaDeNacimiento}
                        {h2.nombre}, que tiene {h2.edad} años y su nacimiento fue en {h2.fechaDeNacimiento}
                        {h3.nombre}, que tiene {h3.edad} años y su nacimiento fue en {h3.fechaDeNacimiento}
                        """)
    