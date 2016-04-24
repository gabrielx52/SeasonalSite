from django.db import models

# Create your models here.


class Produce(models.Model):
    name = models.CharField(max_length=128)
    ideal_temp_low = models.DecimalField(decimal_places=1, max_digits=4)
    ideal_temp_high = models.DecimalField(decimal_places=1, max_digits=4)
    growth_time = models.IntegerField()
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'produce'
        verbose_name_plural = "produce"

    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=16)
    start_date = models.DateTimeField(blank=True, null=False)  # TODO: Add start date
    end_date = models.DateTimeField(blank=True, null=False)  # TODO: Add end date
    produce = models.ManyToManyField(Produce, blank=True, related_name='seasons')

    class Meta:
        verbose_name = 'season'
        verbose_name_plural = "seasons"

    def __str__(self):
        return self.name
