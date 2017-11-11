from django.db import models
from django.conf import settings

# Create your models here.
class Usuario(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	foto = models.ImageField(upload_to='usuario',blank=True, null=True, default='usuario/default.jpg')
	
