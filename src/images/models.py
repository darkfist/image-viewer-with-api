from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save


from .utils import unique_slug_generator

User = settings.AUTH_USER_MODEL

class Image(models.Model):
	uploaded_by	= models.ForeignKey(User)
	title 		= models.CharField(max_length=120, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	image 		= models.ImageField(null=True, blank=True)
	timestamp	= models.DateTimeField(auto_now_add=True)
	updated		= models.DateTimeField(auto_now=True)
	slug 		= models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.title

def image_pre_save_signal(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(image_pre_save_signal, sender=Image)