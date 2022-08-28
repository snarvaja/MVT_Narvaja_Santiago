from datetime import datetime
from django.db import models

# Create your models here.

class Familia(models.Model):

    relacion = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    hijos = models.IntegerField()
    cumpleaños = models.DateField(null=True,blank=True)
