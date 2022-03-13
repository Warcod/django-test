from pyexpat import model
from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    
    
class Curso(models.Model):
    nombre = models.CharField(max_length=30)  
    camada = models.IntegerField()
    
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    profesion = models.CharField(max_length=30)
    email = models.EmailField()
    
    
class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField((""), auto_now=False, auto_now_add=False)
    entregado = models.BooleanField(default=False)

