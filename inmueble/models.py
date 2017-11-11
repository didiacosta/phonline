from django.db import models
from parametrizacion import DBarrio
from parametrizacion import ETipo
from usuarios import Usuario


class FInmueble(models.Model):
	nombre = models.CharField(max_length=255)
	direccion = models.CharField(max_length=255)
	barrio = models.ForeignKey(DBarrio , related_name = 'fk_inmueble_barrio',on_delete=models.PROTECT)
	privado = models.BooleanField(default=True)	#para que es este campo?
	administrador = models.ForeignKey(Usuario , related_name = 'fk_inmueble_administrador',on_delete=models.PROTECT)
	tipo = models.ForeignKey(ETipo , related_name = 'fk_inmueble_tipo',on_delete=models.PROTECT)
	foto = models.ImageField(upload_to='inmueble',blank=True, null=True, default='inmueble/default.jpg')
	longitud = models.CharField(max_length=50)
	latitud = models.CharField(max_length=50)


	class Meta:
		db_table = "Inmueble"
		permissions = (("can_see_inmueble","can see inmueble"),)
		verbose_name='Inmueble'
		unique_together = [
			["nombre",],
		]

	def __unicode__(self):
		return self.nombre