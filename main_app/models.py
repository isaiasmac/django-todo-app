from django.db import models
from django.conf import settings

import datetime

class Task(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200, blank=False)
	details = models.TextField(max_length=500, blank=True)
	date_add = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title