# Python Project Requirements fulfilled 1.Implement a “master loop” console application where the user can repeatedly
# enter commands/perform actions, including choosing to exit the program 2.Create a class, then create at least one
# object of that class and populate it with data. The value of at least one object must be used somewhere in your
# code 3.Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in
# your program 4.Create and call at least 3 functions or methods, at least one of which must return a value that is
# used somewhere else in your code. 5.Connect to an external/3rd party API and read data into your app

# Current Weather Comparison project
# refactor later:
# 1. (done) use loop for entering up to 5 cities and append.
# 2. add basic input validation (empty input, no comma, country validation)
# 3. create build_url() function
# 4. use try/catch and handle exceptions in get_weather(). Output error messages
# 5. (done) create a CityWeatherData class with attributes like temperature, weather_description, etc
# 6. add sorting cities by temperature


import string
import requests
import pycountry
from city import CityWeather
from keys import myWeatherApiKey
from datetime import datetime as dt

welcome_message = 'Welcome to the "Current City Weather Comparison" program!'
decor_str = '*'*len(welcome_message)
print(decor_str + '\n' + welcome_message + "\n" + decor_str)


# https://openweathermap.org/current Access current weather data for any location on Earth.
# Api call by city name and 2-letter country code. Example: 'http://api.openweathermap.org/data/2.5/weather?q=London,UK&appid={API key}'
# For US locations, you can call by city name, state code, and country code.
# i.e there are 27 places named Madison in US. You have to specify the state in this case.
# Example: 'http://api.openweathermap.org/data/2.5/weather?q=Madison,IN,US&appid={API key}'
# For temperature in Fahrenheit use &units=imperial. For temperature in Celsius use &units=metric. Default is in Kelvin.
# OpenWeather uses UTC time zone for all API calls.
def get_current_weather(city_country: string):
    response = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=imperial'.format(city_country,
                                                                                             myWeatherApiKey))
    return response.json()


def validate_country_code(city_input: string):
    city_list = city_input.split(',')
    if len(city_list) == 1:
        print('Please, enter city and 2-letter country code separated by comma. i.e. Paris,FR')
        return False
    elif len(city_list) == 2:
        return is_valid_country_code(city_list[1])
    elif len(city_list) == 3:
        return is_valid_country_code(city_list[2])
    else:
        print('Invalid format')
        return False


def is_valid_country_code(code):
    # strip whitespace from the beginning and end
    country_code = code.strip()
    get_country_data = pycountry.countries.get(alpha_2=country_code)
    if get_country_data is None:
        print("'{}' is invalid 2-letter country code".format(country_code))
        return False
    return True


def add_suffix(i):
    if i == 3:
        return '3rd'
    else:
        return str(i) + 'th'


# start with empty list
cities = []
city = ""
MAX_CITIES = 5
number_of_cities = 1
while number_of_cities <= MAX_CITIES and city != 'done':
    if number_of_cities == 1:
        city = input('Enter 1st city you want to compare (city,2-letter country code) i.e Venice,IT: ')
    elif number_of_cities == 2:
        city = input('Enter 2nd city. You can compare up to 5: ')
    else:
        city = input('Enter {} city (or type "done" if you are done entering): '.format(add_suffix(number_of_cities)))
    # add input validation
    if city.lower() != 'done':
        cities.append(city)
        number_of_cities += 1

# create dictionary
current_weather_dict = {}
for city in cities:
    city_data = get_current_weather(city)
    city_weather = CityWeather(
        city=city,
        timezone=city_data['timezone'],
        temperature=city_data['main']['temp'],
        weather_description=city_data['weather'][0]['description'],
        humidity=city_data['main']['humidity'],
    )
    current_weather_dict[city] = city_weather


def get_current_local_time(city_tz: int):
    current_utc_time_in_seconds = dt.utcnow().timestamp()
    local_time_in_seconds = current_utc_time_in_seconds + city_tz
    formatted_date = dt.fromtimestamp(local_time_in_seconds).strftime("%A, %B %d %Y  %I:%M")
    return formatted_date


def print_city_weather(city_info: CityWeather):
    print(city_info.city)
    print('Current local time: {}'.format(get_current_local_time(city_info.timezone)))
    print('Temperature: {}'.format(city_info.temperature))
    print('Weather description: {}'.format(city_info.weather_description))
    print('Humidity: {}%'.format(city_info.humidity))


for city in cities:
    print('-' * 50)
    print_city_weather(current_weather_dict[city])
