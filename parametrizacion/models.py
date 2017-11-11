from django.db import models


# Create your models here.

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

	def __unicode__(self):
		return self.nombre	

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

	def __unicode__(self):
		return self.nombre	



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

	def __unicode__(self):
		return self.nombre	

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

	def __unicode__(self):
		return self.nombre	

class ETipo(models.Model):
	nombre = models.CharField(max_length=255)
	codigo = models.IntegerField()

	class Meta:
		db_table = "Tipo"
		permissions = (("can_see_tipo","can see tipo"),)
		verbose_name='Tipo'
		unique_together = [
			["nombre",],
		]

	def __unicode__(self):
		return self.nombre	

class FBanco(models.Model):
	nombre = models.CharField(max_length=255)

	class Meta:
		db_table = "Banco"
		permissions = (("can_see_banco","can see banco"),)
		verbose_name='Banco'
		unique_together = [
			["nombre",],
		]

	def __unicode__(self):
		return self.nombre	
