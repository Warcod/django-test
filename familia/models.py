from django.db import models

# Create your models here.


class Hermano(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    fechaDeNacimiento = models.DateField()
    
