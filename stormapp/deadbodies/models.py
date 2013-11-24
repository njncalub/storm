from django.db import models
import os
from uuid import uuid4
from geopy import geocoders

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

    location = models.CharField(max_length=255, verbose_name="Location")
    nlong = models.DecimalField(null=True, blank=True, decimal_places=5, max_digits=15, default=0.00)
    nlat = models.DecimalField(null=True, blank=True, decimal_places=5, max_digits=15, default=0.00)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U')
    image = models.ImageField("Uploaded Image", upload_to=get_upload_path, null=True, blank=True, max_length=150)
    date_reported = models.DateTimeField('Date Reported', auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='N')

    def save(self):
        if self.nlong is None or self.nlat is None:
            nlat = 0.0
            nlong = 0.0
            location = self.location
            g = geocoders.GoogleV3()
            place, (lat, lng) = g.geocode(location)
            print "%s: %.5f, %.5f" % (place, lat, lng)
            self.nlat = lat
            self.nlong = lng
        super(DeadBody, self).save()

    def __unicode__(self):
        return self.gender + " at " + self.location

    class Meta:
        verbose_name_plural = "dead bodies"