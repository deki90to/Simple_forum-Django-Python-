from django.db import models
from datetime import datetime


# Create your models here.

class Posts(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField(null=True, blank=True)
	created = models.DateTimeField(default=datetime.now)
	image = models.ImageField(upload_to='images', null=True, blank=True)
	video = models.FileField(upload_to='videos', null=True, blank=True)


	def __str__(self):
		return f'{self.text}, {self.image}, {self.video}'


	class Meta:
		verbose_name_plural = 'Posts'

	# class Meta:
 #        ordering = ['-created',]