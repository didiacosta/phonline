from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class Persona(models.Model):
	cedula = models.BigIntegerField()
	nombres = models.CharField(max_length=255)
	apellidos = models.CharField(max_length=255)
	correo = models.EmailField(max_length=70,blank=True, null=True)
	telefono = models.CharField(max_length=30,blank=True, null=True)	
	
	def __str__(self):
		return self.nombres + ' ' + self.apellidos

	class Meta:
		db_table = "persona"
		permissions = (("can_see_persona","can see persona"),)
		verbose_name='persona'
		unique_together = [
			['cedula',],['correo',],
		]

