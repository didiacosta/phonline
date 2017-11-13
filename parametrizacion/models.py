from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class APais(models.Model):
	nombre = models.CharField(max_length=255)
	validaNit = models.CharField(max_length=255) #### Para que es este campo????

	class Meta:
		db_table = "Pais"
		permissions = (("can_see_pais","can see pais"),)
		verbose_name='Pais'
		unique_together = [
			["nombre",],
		]

	def __str__(self):
		return self.nombre	

@python_2_unicode_compatible
class BDepartamento(models.Model):
	nombre = models.CharField(max_length=255)
	pais = models.ForeignKey(APais , related_name = 'fk_departamento_pais',on_delete=models.PROTECT)

	class Meta:
		db_table = "Departamento"
		permissions = (("can_see_departamento","can see departamento"),)
		verbose_name='Departamento'
		unique_together = [
			["nombre","pais"],
		]

	def __str__(self):
		return self.nombre	


@python_2_unicode_compatible
class CMunicipio(models.Model):
	nombre = models.CharField(max_length=255)
	departamento = models.ForeignKey(BDepartamento , related_name = 'fk_municipio_departamento',
		on_delete=models.PROTECT)

	class Meta:
		db_table = "Municipio"
		permissions = (("can_see_municipio","can see municipio"),)
		verbose_name='Municipio'
		unique_together = [
			["nombre","departamento"],
		]

	def __str__(self):
		return self.nombre	

	@property
	def pais(self):
		return departamento.pais



@python_2_unicode_compatible
class DBarrio(models.Model):
	nombre = models.CharField(max_length=255)
	municipio = models.ForeignKey(CMunicipio , related_name = 'fk_barrio_municipio',
		on_delete=models.PROTECT)

	class Meta:
		db_table = "Barrio"
		permissions = (("can_see_barrio","can see barrio"),)
		verbose_name='Barrio'
		unique_together = [
			["nombre","municipio"],
		]

	def __str__(self):
		return self.nombre	

	@property
	def pais(self):
		return municipio.departamento.pais

	@property
	def departamento(self):
		return municipio.departamento


@python_2_unicode_compatible
class ETipo(models.Model):
	nombre = models.CharField(max_length=255)
	codigo = models.IntegerField()
	modelo = models.ForeignKey(ContentType, on_delete=models.PROTECT, related_name='fk_tipo_modelo')

	class Meta:
		db_table = "Tipo"
		permissions = (("can_see_tipo","can see tipo"),)
		verbose_name='Tipo'
		unique_together = [
			["nombre",],
		]

	def __str__(self):
		return self.nombre	

@python_2_unicode_compatible
class FBanco(models.Model):
	nombre = models.CharField(max_length=255)

	class Meta:
		db_table = "Banco"
		permissions = (("can_see_banco","can see banco"),)
		verbose_name='Banco'
		unique_together = [
			["nombre",],
		]

	def __str__(self):
		return self.nombre	
