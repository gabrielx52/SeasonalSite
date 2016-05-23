from django.test import TestCase
from seasonal.models import *

# Create your tests here.


class ProduceTestCase(TestCase):
    produce_fields = {'name': "banana",
                      'ideal_temp_low': 0.1,
                      'ideal_temp_high': 999.9,
                      'growth_time': 15,
                      'grow_zone': 5,
                      'description': "This is a test fruit or veggie."
                      }

    produce = Produce(**produce_fields)

    def setup(self):
        pass  # No setup needed at this time.

    def test_string_representation(self):
        self.assertEqual(self.produce_fields['name'], str(self.produce))

    def test_produce_attributes(self):
        self.assertEqual(self.produce_fields['name'], self.produce.name)
        self.assertEqual(self.produce_fields['ideal_temp_low'], self.produce.ideal_temp_low)
        self.assertEqual(self.produce_fields['ideal_temp_high'], self.produce.ideal_temp_high)
        self.assertEqual(self.produce_fields['growth_time'], self.produce.growth_time)
        self.assertEqual(self.produce_fields['grow_zone'], self.produce.grow_zone)
        self.assertEqual(self.produce_fields['description'], self.produce.description)


class LocationTestCase(TestCase):
    location_fields = {'zipcode': 98105,
                       'city': "Seattle",
                       'state': "Washington",
                       'grow_zone': "5",
                       'airport_zone': "SEATAC"
                       }

    location = Location(**location_fields)

    def setup(self):
        pass  # No setup needed at this time.

    def test_string_representation(self):
        expected = "{}, {}".format(self.location_fields['city'], self.location_fields['state'])
        self.assertEqual(expected, str(self.location))

    def test_location_attributes(self):
        self.assertEqual(self.location_fields['zipcode'], self.location.zipcode)
        self.assertEqual(self.location_fields['city'], self.location.city)
        self.assertEqual(self.location_fields['state'], self.location.state)
        self.assertEqual(self.location_fields['grow_zone'], self.location.grow_zone)
        self.assertEqual(self.location_fields['airport_zone'], self.location.airport_zone)
