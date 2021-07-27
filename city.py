import datetime


def get_current_local_time(tz: int):
    local = datetime.datetime.utcnow() + datetime.timedelta(seconds=tz)
    formatted_local_date_time = local.strftime("%A, %B %d %Y  %I:%M%p")
    return formatted_local_date_time


def add_emoji(weather_description):
    if 'cloud' in weather_description:
        return "\N{cloud}"
    elif 'thunderstorm' in weather_description:
        return "\U000026A1"
    elif 'rain' in weather_description:
        return "\N{umbrella with rain drops}"
    elif 'snow' in weather_description:
        return "\N{snowflake}"
    elif 'clear' in weather_description:
        return "\N{slightly smiling face}"
    else:
        return "\N{thinking face}"


class CityWeather:

    def __init__(self, city, country_code, timezone, temperature, weather_description, humidity):
        self.city = city,
        self.country_code = country_code,
        self.timezone = timezone  # shift in seconds from UTC
        self.temperature = temperature
        self.weather_description = weather_description
        self.humidity = humidity

    def print_city_weather(self):
        print(str(*self.city).upper(), *self.country_code)
        # OpenWeather uses UTC time zone for all API calls. We want local time in each city
        print('Current local time: {}'.format(get_current_local_time(self.timezone)))
        print('Temperature: {}'.format(self.temperature))
        print('Weather description: {} '.format(self.weather_description), end='')
        print(add_emoji(self.weather_description))
        print('Humidity: {}%'.format(self.humidity))
