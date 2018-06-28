from django.contrib import admin

from .models import Organizador
from .models import Evento
from .models import Invitado
from .models import Padrino
from .models import Carousel

admin.site.register(Organizador)
admin.site.register(Evento)
admin.site.register(Invitado)
admin.site.register(Padrino)
admin.site.register(Carousel)
