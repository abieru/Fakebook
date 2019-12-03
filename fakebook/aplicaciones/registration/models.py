from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to='profiles', null=True, blank=True)
	portada = models.ImageField(upload_to='portadas', null=True, blank=True)
	bio = models.TextField(verbose_name="Biografia", null=True, blank=True)