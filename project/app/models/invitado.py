from django.db import models

class Invitado(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    apellido = models.CharField(max_length=100, blank=False, null=False)
    mail = models.CharField(max_length=100, blank=False, null=False)
    asistencia = models.BooleanField(default=False)
    token = models.CharField(max_length=100)

	def __str__(self):
		return "{} {}". format(self.nombre, self.apellido or "")