from django.contrib import admin
from parametrizacion.models import APais,BDepartamento,CMunicipio,DBarrio,ETipo, FBanco
# Register your models here.

class AdminPais(admin.ModelAdmin):
	list_display=('nombre','validaNit')
	search_fields=('nombre',)

admin.site.register(APais,AdminPais)

class AdminDepartamento(admin.ModelAdmin):
	list_display=('pais','nombre',)
	search_fields=('nombre',)
	list_filter=('pais',)

admin.site.register(BDepartamento,AdminDepartamento)

class AdminMunicipio(admin.ModelAdmin):
	list_display=('pais','departamento','nombre',)
	search_fields=('nombre',)
	list_filter=('departamento',)

admin.site.register(CMunicipio,AdminMunicipio)

class AdminBarrio(admin.ModelAdmin):
	list_display=('pais','departamento','municipio','nombre',)
	search_fields=('nombre',)
	list_filter=('municipio',)

admin.site.register(DBarrio,AdminBarrio)


class AdminTipo(admin.ModelAdmin):
	list_display=('nombre','codigo','modelo',)
	search_fields=('nombre','codigo')
	list_filter=('modelo',)

admin.site.register(ETipo,AdminTipo)

class AdminBanco(admin.ModelAdmin):
	list_display=('nombre',)
	search_fields=('nombre',)

admin.site.register(FBanco,AdminBanco)

