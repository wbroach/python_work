import unittest
from city_functions import get_formatted_city_name

class FormattedCityNameTestCase(unittest.TestCase):
    """ Tests for 'city_functions.py'."""
    
    def test_city_country(self):
        """Does the function return the correctly formatted city name?"""
        city = get_formatted_city_name('santiago', 'chile')
        self.assertEqual(city, 'Santiago, Chile')

    def test_city_country_population(self):
        """
        Does the function return the correctly formatted name w/population?
        """
        city = get_formatted_city_name('santiago', 'chile', population=5000)
        self.assertEqual(city, 'Santiago, Chile - Population: 5000')

unittest.main()
