from django.contrib import admin
from seasonal.models import Produce, Location

# Register your models here.

class LocationAdmin(admin.ModelAdmin):
    """ Location admin """
    list_filter = ['state', 'grow_zone']


admin.site.register(Produce)
admin.site.register(Location, LocationAdmin)
