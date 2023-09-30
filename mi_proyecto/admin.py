from django.contrib import admin

from .models import Estudiante,Materia,Nota

admin.site.register(Estudiante)
admin.site.register(Materia)
admin.site.register(Nota)