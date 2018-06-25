from django.db import models

class Carousel(models.Model):
    foto = models.ImageField(upload_to='padrinos/%Y/%m/%d', default = 'sin-imagen/no-img.jpg')
    nombre = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.foto.name