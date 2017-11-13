from django.contrib import admin
from persona.models import Persona
# Register your models here.
class AdminPersona(admin.ModelAdmin):
	list_display=('cedula','nombres','apellidos','correo','telefono')
	search_fields=('nombres','apellidos','correo','cedula')

admin.site.register(Persona,AdminPersona)