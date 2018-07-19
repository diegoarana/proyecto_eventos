from __future__ import unicode_literals
from django.db import models
from .evento import Evento

class Invitado(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    nombre_apellido = models.CharField(max_length=100, blank=False)
    mail = models.CharField(max_length=100, blank=False)
    mensaje = models.TextField(blank=False, max_length=100)

    def __str__(self):
        return self.nombre_apellido