from django.db import models
from django.utils import timezone


class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField(default=timezone.now)
	create_date = models.DateTimeField(blank=True, null=True)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = tomezone.now()
		self.save()

	def __str__(self):
		return self.title
