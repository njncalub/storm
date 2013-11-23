from django.db import models
import os
from uuid import uuid4

# Create your models here.

class DeadBody(models.Model):
    GENDER_CHOICES = (
        ('U', 'Unknown'),
        ('M', 'Male'),
        ('F', 'Female'),
    )

    STATUS_CHOICES = (
        ('N', 'New'),
        ('R', 'Retrieved'),
    )

    def get_upload_path(instance, filename):
        fname, dot, extension = filename.rpartition('.')
        new_name = '%s.%s' % (str(uuid4().hex), extension)
        return os.path.join("uploaded", "images", new_name)

    location = models.CharField(max_length=255, null=True, blank=True, verbose_name="Location")
    #nlong = models.FloatField(null=True, blank=True)
    #nlat = models.FloatField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U')
    image = models.ImageField("Uploaded Image", upload_to=get_upload_path, null=True, blank=True, max_length=150)
    date_reported = models.DateTimeField('Date Reported', auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='N')

    def __unicode__(self):
        return self.gender + " at " + self.location

    class Meta:
        verbose_name_plural = "dead bodies"