class CityWeather:

    def __init__(self, city, timezone, temperature, weather_description, humidity):
        self.city = city
        self.timezone = timezone  # shift in seconds from UTC
        self.temperature = temperature
        self.weather_description = weather_description
        self.humidity = humidity
