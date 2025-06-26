# This file performs unit tests on the city_country function.
import unittest
from city_functions import city_country

def test_city_country():
        """Test that city and country are formatted correctly."""
        formatted = city_country('paris', 'france')
        assert formatted == 'Paris, France'


