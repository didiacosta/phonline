from django.contrib import admin
from inmueble.models import AInmueble, BCuentaInmueble, CNoticia, DDocumento, EIndicador, FVivienda, GResidente
# Register your models here.

class AdminInmueble(admin.ModelAdmin):
	list_display=('nombre','direccion','barrio','privado','administrador','tipo','longitud','latitud','foto_inmueble')
	search_fields=('nombre','barrio','direccion',)
	#list_filter=('pais','departamento','municipio')

admin.site.register(AInmueble,AdminInmueble)


class AdminCuentaInmueble(admin.ModelAdmin):
	list_display=('inmueble','banco','tipo','noCuenta','nombre','activa')
	search_fields=('nombre','noCuenta')
	list_filter=('tipo','activa')

admin.site.register(BCuentaInmueble,AdminCuentaInmueble)

class AdminNoticia(admin.ModelAdmin):
	list_display=('inmueble','titulo','descripcionCompacta','foto_noticia','activa')
	search_fields=('titulo','descripcion')
	list_filter=('activa',)

admin.site.register(CNoticia,AdminNoticia)

class AdminDocumento(admin.ModelAdmin):
	list_display=('inmueble','titulo','archivo','tipo','activo')
	search_fields=('titulo',)
	list_filter=('activo',)

admin.site.register(DDocumento,AdminDocumento)

class AdminIndicador(admin.ModelAdmin):
	list_display=('nombre',)
	search_fields=('nombre',)

admin.site.register(EIndicador,AdminIndicador)

class AdminVivienda(admin.ModelAdmin):
	list_display=('inmueble','tipo','indicador','nombreIndicador','indicador2','nombreIndicador2','activo')
	search_fields=('nombreIndicador','nombreIndicador2')
	list_filter=('activo','tipo','indicador','indicador2')

admin.site.register(FVivienda,AdminVivienda)

class AdminResidente(admin.ModelAdmin):
	list_display=('inmueble','vivienda','persona','tipo','activo')
	search_fields=('persona','vivienda')
	list_filter=('tipo','activo')

admin.site.register(GResidente,AdminResidente)

