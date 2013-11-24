from django.db import models
import os
from geopy import geocoders

# Create your models here.

class ReliefOps(models.Model):
    location = models.CharField(max_length=255, verbose_name="Location")
    nlong = models.DecimalField(null=True, blank=True, decimal_places=5, max_digits=15, default=0.00)
    nlat = models.DecimalField(null=True, blank=True, decimal_places=5, max_digits=15, default=0.00)

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
        super(ReliefOps, self).save()

    def __unicode__(self):
        return self.location

    class Meta:
        verbose_name_plural="Relief Operations"