from django.db import models
from django.conf import settings
from parametrizacion.models import ETipo
from persona.models import Persona
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.
@python_2_unicode_compatible
class Usuario(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	persona = models.ForeignKey(Persona , related_name = 'fk_usuario_persona',on_delete=models.PROTECT)	
	foto = models.ImageField(upload_to='usuario',blank=True, null=True, default='usuario/default.jpg')
	tipo = models.ForeignKey(ETipo , related_name = 'fk_usuario_tipo',
		on_delete=models.PROTECT)

	class Meta:
		db_table = "usuario"
		permissions = (("can_see_usuario","can see usuario"),)
		verbose_name='usuario'

	def __str__(self):
		return self.user.username


	def foto_usuario(self):
		  return """<img width="100px" height="120px" src="%s" alt="foto del usuario">""" % self.foto.url

	foto_usuario.allow_tags=True

