from django.db import models
# Create your models here.
class Proyecto(models.Model):
    fechaSalida = models.DateField()
    nombre = models.CharField(max_length = 50)
    Genero = models.CharField(max_length = 50)
    Precio = models.IntegerField()
    Pegi = models.CharField(max_length = 50)
    Plataforma = models.CharField(max_length = 50)