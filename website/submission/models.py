from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Submission(models.Model):
	sub_id = models.CharField(max_length=5, default=0)
	sub_title = models.CharField(max_length=30)
	#author = models.ForeignKey()
	#link to customUser

	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	comments = models.TextField()
	#upvotes = models.
	#downvotes = models.
	num_views = models.PositiveSmallIntegerField()
	category = models.CharField(max_length=50)

	def post(self):
		self.published_date = timezone.now()
		self.save()


