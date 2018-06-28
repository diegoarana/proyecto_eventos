from __future__ import unicode_literals
from django.db import models
from .evento import Evento

class Carousel(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='padrinos/%Y/%m/%d', default = 'sin-imagen/no-img.jpg')
    nombre = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.foto.name