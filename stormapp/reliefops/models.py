from django.db import models
import os
from uuid import uuid4

# Create your models here.

class ReliefOps(models.Model):
	location = models.CharField(max_length=255, null = True, blank=True, verbose_name("Location"))
	nlong = models.DecimalField(null=True, blank=True, decimal_places=5, max_digits=15, default=0.00)
	nlat = models.DecimalField(null=True, blank=True, decimal_places=5, max_digits=15, default=0.00)

	def __unicode__(self):
		return self.location

	class Meta:
		verbose_name_plural="Relief Operations"