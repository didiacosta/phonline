from django.db import models
from parametrizacion.models import DBarrio
from parametrizacion.models import ETipo, FBanco, CMunicipio
from usuarios.models import Usuario
from persona.models import Persona
from django.template.defaultfilters import truncatechars
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class AInmueble(models.Model):
	nombre = models.CharField(max_length=255)
	direccion = models.CharField(max_length=255)
	barrio = models.ForeignKey(DBarrio , related_name = 'fk_inmueble_barrio',on_delete=models.PROTECT)
	privado = models.BooleanField(default=True)	#para que es este campo?
	administrador = models.ForeignKey(Usuario , related_name = 'fk_inmueble_administrador',on_delete=models.PROTECT)
	tipo = models.ForeignKey(ETipo , related_name = 'fk_inmueble_tipo',on_delete=models.PROTECT)
	foto = models.ImageField(upload_to='inmueble',blank=True, null=True, default='inmueble/default.jpg')
	longitud = models.CharField(max_length=50)
	latitud = models.CharField(max_length=50)

	@property
	def pais(self):
		return barrio.municipio.departamento.pais

	@property
	def departamento(self):
		return barrio.municipio.departamento

	@property
	def municipio(self):
		return barrio.municipio


	class Meta:
		db_table = "inmueble_Inmueble"
		permissions = (("can_see_inmueble","can see inmueble"),)
		verbose_name='Inmueble'
		unique_together = [
			["nombre",],
		]

	def __str__(self):
		return self.nombre

	def foto_inmueble(self):
		  return """<img width="100px" height="120px" src="%s" alt="foto del inmueble">""" % self.foto.url

	foto_inmueble.allow_tags=True

@python_2_unicode_compatible
class BCuentaInmueble(models.Model):
	inmueble = models.ForeignKey(AInmueble , related_name = 'fk_cuentaInmueble_inmueble',
		on_delete=models.PROTECT) # Creo que falto este campo en el diseño
	banco = models.ForeignKey(FBanco , related_name = 'fk_cuentaInmueble_banco',on_delete=models.PROTECT)
	municipio = models.ForeignKey(CMunicipio , related_name = 'fk_cuentaInmueble_municipio',
		on_delete=models.PROTECT)
	tipo = models.ForeignKey(ETipo , related_name = 'fk_cuentaInmueble_tipo',on_delete=models.PROTECT)
	activa = models.BooleanField(default=True)
	noCuenta = models.CharField(max_length=50)
	nombre  = models.CharField(max_length=100)

	class Meta:
		db_table = "inmueble_cuentaInmueble"
		permissions = (("can_see_cuentaInmueble","can see cuentaInmueble"),)
		verbose_name='cuentaInmueble'
		unique_together = [
			["nombre",],
		]

	def __str__(self):
		return self.nombre

@python_2_unicode_compatible
class CNoticia(models.Model):
	inmueble = models.ForeignKey(AInmueble , related_name = 'fk_noticia_inmueble', on_delete=models.PROTECT)
	titulo = models.CharField(max_length=150)
	descripcion = models.TextField()
	foto =  models.ImageField(upload_to='noticia',blank=True, null=True, default='noticia/default.jpg')
	activa = models.BooleanField(default=True)

	class Meta:
		db_table = "inmueble_noticia"
		permissions = (("can_see_notifica","can see notifica"),)
		verbose_name='noticia'
		unique_together = [
			["inmueble","titulo"],
		]

	def __str__(self):
		return self.titulo

	@property
	def descripcionCompacta(self):
		return truncatechars(self.titulo, 50)

	def foto_noticia(self):
		  return """<img width="100px" height="120px" src="%s" alt="foto de la noticica">""" % self.foto.url

	foto_noticia.allow_tags=True

@python_2_unicode_compatible
class DDocumento(models.Model):
	inmueble = models.ForeignKey(AInmueble , related_name = 'fk_documento_inmueble', on_delete=models.PROTECT)
	titulo = models.CharField(max_length=100)
	documento = models.FileField(upload_to='documentos')
	tipo = models.ForeignKey(ETipo , related_name = 'fk_documento_tipo',on_delete=models.PROTECT)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return self.nombre

	def archivo(self):
		return """<a href="%s">archivo</a> """ % self.documento.url

	archivo.allow_tags = True

	class Meta:
		db_table = "inmueble_documento"
		permissions = (("can_see_documento","can see documento"),)
		verbose_name='documento'
		unique_together = [
			["titulo",],
		]

@python_2_unicode_compatible
class EIndicador(models.Model):
	nombre = models.CharField(max_length=20)

	def __str__(self):
		return self.nombre

	class Meta:
		db_table = "inmueble_indicador"
		permissions = (("can_see_indicador","can see indicador"),)
		verbose_name='indicador'
		unique_together = [
			["nombre",],
		]

@python_2_unicode_compatible
class FVivienda(models.Model):
	inmueble = models.ForeignKey(AInmueble , related_name = 'fk_vivienda_inmueble', on_delete=models.PROTECT)	
	tipo = models.ForeignKey(ETipo , related_name = 'fk_vivienda_tipo',on_delete=models.PROTECT)
	indicador = models.ForeignKey(EIndicador , related_name = 'fk_vivienda_indicador1', on_delete=models.PROTECT)
	nombreIndicador = models.CharField(max_length=50)
	indicador2 = models.ForeignKey(EIndicador , related_name = 'fk_vivienda_indicador2', on_delete=models.PROTECT,
		blank=True, null=True)
	nombreIndicador2 = models.CharField(max_length=50,blank=True, null=True)	
	activo = models.BooleanField(default=True)

	def __str__(self):
		retorno=self.indicador.nombre + ' ' + self.nombreIndicador
		if self.indicador2 and self.nombreIndicador2:
			retorno = retorno + ' ' + indicador2.nombre + ' ' + self.nombreIndicador2
		return retorno

	class Meta:
		db_table = "inmueble_vivienda"
		permissions = (("can_see_vivienda","can see vivienda"),)
		verbose_name='vivienda'
		unique_together = [
			["nombreIndicador","nombreIndicador2"],
		]

@python_2_unicode_compatible
class GResidente(models.Model):
	vivienda = models.ForeignKey(FVivienda , related_name = 'fk_residente_vivienda', on_delete=models.PROTECT)
	tipo = models.ForeignKey(ETipo , related_name = 'fk_residente_tipo',on_delete=models.PROTECT)
	persona = models.ForeignKey(Persona , related_name = 'fk_residente_persona', on_delete=models.PROTECT)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return vivienda +' >> '+persona

	@property
	def inmueble(self):
		return vivienda.inmueble


	class Meta:
		db_table = "inmueble_residente"
		permissions = (("can_see_residente","can see residente"),)
		verbose_name='residente'
		unique_together = [
			["vivienda","persona","activo"],
		]

		
