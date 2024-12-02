import unittest
from city_functions import city_country

class TestCityCountryFunction(unittest.TestCase):

    def test_city_country(self):
        # Tests that the function returns the correct formatted string
        self.assertEqual(city_country("Santiago", "Chile"), "Santiago, Chile")
        self.assertEqual(city_country("New York", "USA"), "New York, USA")
        self.assertEqual(city_country("Tokyo", "Japan"), "Tokyo, Japan")

if __name__ == '__main__':
    unittest.main()