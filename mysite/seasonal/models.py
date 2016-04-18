from django.db import models

# Create your models here.


class Produce(models.Model):
    name = models.CharField(max_length=128)
    ideal_temp = models.DecimalField(decimal_places=1, max_digits=4)
    growth_time = models.DurationField()
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'produce'
        verbose_name_plural = "produce"

    def __str__(self):
        return self.name


class Spring(models.Model):
    name = 'Spring'
    start_date = models.DateTimeField(blank=True, null=True) # TODO: Add start date
    end_date = models.DateTimeField(blank=True, null=True) # TODO: Add end date
    seasonal_produce = models.ManyToManyField(Produce, blank=True)


class Summer(models.Model):
    name = 'Summer'
    start_date = models.DateTimeField(blank=True, null=True) # TODO: Add start date
    end_date = models.DateTimeField(blank=True, null=True) # TODO: Add end date
    seasonal_produce = models.ManyToManyField(Produce, blank=True)


class Fall(models.Model):
    name = 'Fall'
    start_date = models.DateTimeField(blank=True, null=True) # TODO: Add start date
    end_date = models.DateTimeField(blank=True, null=True) # TODO: Add end date
    seasonal_produce = models.ManyToManyField(Produce, blank=True)


class Winter(models.Model):
    name = 'Winter'
    start_date = models.DateTimeField(blank=True, null=True) # TODO: Add start date
    end_date = models.DateTimeField(blank=True, null=True) # TODO: Add end date
    seasonal_produce = models.ManyToManyField(Produce, blank=True)
