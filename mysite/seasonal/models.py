from django.db import models

# Create your models here.


class Produce(models.Model):
    """
    Django model representing fruits and vegetables.
    
    Attributes:
        name: A string representation of the object.
        ideal_temp_low: A decimal representation of the low ideal temperature range(in degrees F).
        ideal_temp_high: A decimal representation of the high ideal temperature range (in degrees F).
        growth_time: Integer representation of the grow time (in days).
        description: A text description of the object.
    """
    name = models.CharField(max_length=128)
    ideal_temp_low = models.DecimalField(decimal_places=1, max_digits=4)
    ideal_temp_high = models.DecimalField(decimal_places=1, max_digits=4)
    growth_time = models.IntegerField()
    grow_zone = models.CharField(max_length=32)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'produce'
        verbose_name_plural = "produce"

    def __str__(self):
        """ String representation of the object."""
        return self.name


class Location(models.Model):
    """
    Django model representing a location.

    Attributes:
        zipcode: String representing the zip code.
        city: String representing the city.
        state: String representing the state.
        grow_zone: String representing the grow zones.
        airport_zone: String representing hte airport zone.
    """
    zipcode = models.CharField(max_length=5)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=32)
    grow_zone = models.CharField(max_length=8)
    airport_zone = models.CharField(max_length=8, null=True, blank=True)

    class Meta:
        verbose_name = 'location'
        verbose_name_plural = "locations"

    def __str__(self):
        """ String representation of the object in (city), (state) format."""
        return "{}, {}".format(self.city, self.state)
