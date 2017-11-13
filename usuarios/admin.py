from django.contrib import admin
from usuarios.models import Usuario
# Register your models here.

class AdminUsuario(admin.ModelAdmin):
	list_display=('user','persona','foto_usuario')
	search_fields=('user__username',)
	list_filter=('tipo',)

admin.site.register(Usuario,AdminUsuario)