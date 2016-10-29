from django.db import models
from django.utils import timezone
# Create your models here.
class Article(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length = 25)
	body = models.CharField(max_length = 255)
	conclusion = models.CharField(max_length = 200)
	publishedDate = models.DateTimeField('Date published')

	def __str__(self):
		return  self.title

class Poll(models.Model):
	comment = models.CharField(max_length = 250)
	like = models.CharField(max_length=200)

	def __str__(self):
		return self.comment