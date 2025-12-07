## Student ID:
## Student Name: Raja Sumeer
## Unit Test
import unittest

#importing weather class from weather module
from WeatherClass import WeatherData

#create test case that inherits from 'unittest.TestCase'
class TestWeather(unittest.TestCase):
    def test_conditions(self):
        print('test weather conditions')
        # Average numbers for C, km/h, hPa and mm
        weather = WeatherData(15, 29, 1013, 0)
        self.assertEqual(weather.get_temp(), 15)
        self.assertEqual(weather.get_wind(), 29)
        self.assertEqual(weather.get_pressure(), 1013)
        self.assertEqual(weather.get_rain(), 0)
    
    def test_is_raining(self):
        print('test rain status')
        weather = WeatherData(15, 29, 1013, 0)
        self.assertEqual(weather.is_raining(), True)

if __name__ == '__main__':
    unittest.main()