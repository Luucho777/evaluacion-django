from django.contrib import admin

from apps.el_progreso.models import Entrenador, Actividad, Espacio, Evento, Socio

admin.site.register(Entrenador)
admin.site.register(Actividad)
admin.site.register(Espacio)
admin.site.register(Evento)
admin.site.register(Socio)
