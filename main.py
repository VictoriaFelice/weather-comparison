# CodeLouisville Python Project Requirements Fulfilled
# 1.Implement a “master loop” console application where the user can repeatedly enter commands/perform actions.
# 2.Create a class, then create at least one object of that class and populate it with data.
# 3.Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program.
# 4.Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code.
# 5.Connect to an external/3rd party API and read data into your app.

# later:
# 1. add basic input validation (empty input, no comma, country validation)
# 2. add weather emoji for weather_descriptions (print("\U00002600"))

import string
import requests

from city import CityWeather
from keys import myWeatherApiKey

decor_length = 100


def print_decor(element: string, length: int):
    print(element * length)


def print_welcome_message():
    welcome_message = 'Welcome to the "Current City Weather Comparison" program!'
    spacing = ' ' * int(((decor_length - len(welcome_message)) / 2))
    print(len(spacing))
    print_decor('*', decor_length)
    print(spacing + welcome_message)
    print_decor('*', decor_length)


print_welcome_message()


# https://openweathermap.org/current Access current weather data for any location on Earth.
# Api call by city name and 2-letter country code. Example: 'http://api.openweathermap.org/data/2.5/weather?q=,FR&appid={API key}'
# For US locations, you can call by city name, state code, and country code.
# i.e there are 27 places named Madison in US. You have to specify the state in this case.
# Example: 'http://api.openweathermap.org/data/2.5/weather?q=Madison,IN,US&appid={API key}'
# For temperature in Fahrenheit use &units=imperial. For temperature in Celsius use &units=metric. Default is in Kelvin.
# OpenWeather uses UTC time zone for all API calls.
def get_current_weather(city_country: string):
    response = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=imperial'.format(city_country,
                                                                                             myWeatherApiKey)).json()
    response_code = response['cod']
    if response_code != 200:
        print('\n!! ERROR')
        if 'invalid' in response['message'].lower():
            print(response['message'])
            exit()
        elif 'city' in response['message'].lower():
            print(city_country + ': ', end='')
        print(response['message'])
        return None
    return response


def add_suffix(i):
    if i == 3:
        return '3rd'
    else:
        return str(i) + 'th'


# create current weather dictionary where key is city and value is CityWeather class instance
def create_current_weather_dictionary(cites_with_countries):
    current_weather_dict = {}
    for city_country in cites_with_countries:
        response = get_current_weather(city_country)
        if response is not None:
            city_weather = CityWeather(
                city=response['name'],
                country_code=response['sys']['country'],
                timezone=response['timezone'],
                temperature=response['main']['temp'],
                weather_description=response['weather'][0]['description'],
                humidity=response['main']['humidity']
            )
            current_weather_dict[city_country] = city_weather
    return current_weather_dict


# sort cities by the warmest current temperature
def sort_cities_by_temp(current_weather_dict):
    sorted_cities = sorted(current_weather_dict, key=lambda c: current_weather_dict[c].temperature, reverse=True)
    sorted_city_weather_dict = {}
    for cty in sorted_cities:
        sorted_city_weather_dict[cty] = current_weather_dict[cty]
    return sorted_city_weather_dict


def output_results(sorted_city_weather_dict):
    print_decor('=', decor_length)
    print("Currently, the warmest city is {}. \nColdest city is {}.".format(next(iter(sorted_city_weather_dict)), (next(reversed(sorted_city_weather_dict)))))
    print_decor('=', decor_length)
    for cty in sorted_city_weather_dict:
        CityWeather.print_city_weather(sorted_city_weather_dict[cty])
        print('-' * decor_length)


# master loop
while True:
    cities = []
    city = ""
    max_cities = 5
    number_of_cities = 1
    while number_of_cities <= max_cities and city != 'd' and city != 'q':
        if number_of_cities == 1:
            city = input(
                "Enter [City,2-letter Country Code] i.e Venice,IT\nFor US locations, enter [City,State,US] i.e Louisville,KY,US: ")
        elif number_of_cities == 2:
            city = input('Enter 2nd city in the same format. You can compare up to 5 cities: ')
        else:
            city = input('Enter {} city (or type "d" if you are done entering): '.format(add_suffix(number_of_cities)))
        # add input validation later
        if city.lower() != 'd':
            cities.append(city)
            number_of_cities += 1

    weather = create_current_weather_dictionary(cities)
    if weather:
        sorted_city_weather = sort_cities_by_temp(weather)
        output_results(sorted_city_weather)

    yes_no = input("Do you want to enter new cities? Type 'y' to continue or 'q' to quit: ")
    if 'q' in yes_no.lower():
        exit()
    print()

# implement later
# def validate_country_code(city_input: string):
#     city_list = city_input.split(',')
#     if len(city_list) == 1:
#         print('Please, enter city and 2-letter country code separated by comma. i.e. Paris,FR')
#         return False
#     elif len(city_list) == 2:
#         return is_valid_country_code(city_list[1])
#     elif len(city_list) == 3:
#         return is_valid_country_code(city_list[2])
#     else:
#         print('Invalid format')
#         return False
#
#
# def is_valid_country_code(code):
#     # strip whitespace from the beginning and end
#     country_code = code.strip()
#     get_country_data = pycountry.countries.get(alpha_2=country_code)
#     if get_country_data is None:
#         print("'{}' is invalid 2-letter country code".format(country_code))
#         return False
#     return True
