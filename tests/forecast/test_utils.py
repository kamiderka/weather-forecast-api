import unittest

from src.forecast.utils import (
    validateCoordinates,
    buildForecastQueryParams,
)

class TestFunctions(unittest.TestCase):

    def test_validateCoordinates(self):
        self.assertTrue(validateCoordinates(45.0, 0.0)[0])

        self.assertFalse(validateCoordinates(-100.0, 0.0)[0])

        self.assertFalse(validateCoordinates(45.0, 200.0)[0])

    def test_buildForecastQueryParams(self):
        latitude = 40.0
        longitude = -75.0
        expected_params = {
            "latitude": latitude,
            "longitude": longitude,
            "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "sunshine_duration"]
        }
        self.assertEqual(buildForecastQueryParams(latitude, longitude), expected_params)

if __name__ == '__main__':
    unittest.main()
