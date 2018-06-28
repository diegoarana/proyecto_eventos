from __future__ import unicode_literals
from django.db import models
from .organizador import Organizador

class Evento(models.Model):
    organizador = models.OneToOneField(Organizador, on_delete=models.CASCADE, related_name="organizador")
    nombre = models.CharField(max_length=100, blank=False, null=False)
    agasajado = models.CharField(max_length=100, blank=False, null=False)
    direccion = models.CharField(max_length=100, blank=False, null=False)
    fecha = models.DateField(blank=False, null=False)
    hora = models.TimeField(blank=False, null=False)
    foto_principal = models.ImageField(upload_to='principal/%Y/%m/%d', default = 'sin-imagen/no-img.jpg')
    foto_secundaria = models.ImageField(upload_to='secundaria/%Y/%m/%d', default = 'sin-imagen/no-img.jpg')

    def __str__(self):
        return "{} : {}". format(self.nombre, self.agasajado or "")