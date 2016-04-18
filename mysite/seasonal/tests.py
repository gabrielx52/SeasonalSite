from django.test import TestCase
from seasonal.models import Produce

# Create your tests here.


class ProduceTestCase(TestCase):

    def setup(self):
        pass # No test setup needed yet.

    def test_string_representation(self):
        expected = "banana"
        p = Produce(name=expected)
        actual = str(p)
        self.assertEqual(expected, actual)
