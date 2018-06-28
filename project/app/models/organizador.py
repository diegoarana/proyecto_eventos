# -*- coding: UTF-8-*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Organizador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="usuario")

    def __str__(self):
        return self.user.username