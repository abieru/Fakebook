from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(verbose_name="Título", max_length=100, null=True, blank=True)
	content = RichTextField(verbose_name="Contenido", null=True, blank=True)
	image = models.ImageField(verbose_name="Imagen", upload_to="Post_img", null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
	updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de creación")

	class Meta:
		verbose_name = 'Publicación'
		verbose_name_plural = 'publicaciones'
		ordering = ['-created']	
 