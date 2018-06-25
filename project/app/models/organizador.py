from django.db import models

class Organizador(models.Model):
    nombre = models.CharField(max_length=100, blank=false, null=false)
    apellido = models.CharField(max_length=100, blank=false, null=false)
    mail = models.CharField(max_length=100, blank=false, null=false)
    telefono = models.PositiveIntegerField(help_text="(Solamente dígitos)", validators=[MaxValueValidator(999999999999999)], blank=False, null=False,)

	def __str__(self):
		return "{} {}". format(self.nombre, self.apellido or "")