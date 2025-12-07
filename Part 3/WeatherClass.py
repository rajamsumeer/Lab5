## Student ID:
## Student Name: Raja Sumeer
## Weather Class
class WeatherData:
    """Weather data class"""
    def __init__(self, temperature, wind, pressure, rain):
        self.temperature = temperature # C
        self.wind = wind # km/h
        self.pressure = pressure #hPa
        self.rain = rain # mm

    # methods that returns weather conditions
    def get_temp(self):
        return self.temperature

    def get_wind(self):
        return self.wind

    def get_pressure(self):
        return self.pressure

    def get_rain(self):
        return self.rain

    def is_raining(self):
        """Return true if rainfall greater than 0mm"""
        return self.rain > 0