## "Current City Weather Comparison" console app :sun_behind_rain_cloud:
### Description:
- To access current weather data for any location on Earth, I am using OpenWeather Api https://openweathermap.org/current
- Api call is done by city name and 2-letter country code. Example: 'http://api.openweathermap.org/data/2.5/weather?q=,FR&appid={API key}'
- For US locations, it is recommended to call by city name, state code, and country code. i.e., there are 27 places named Madison in US.
You have to specify the state in this case. Example: 'http://api.openweathermap.org/data/2.5/weather?q=Madison,IN,US&appid={API key}'
- For temperature in Fahrenheit use &units=imperial. For temperature in Celsius use &units=metric. Default is in Kelvin.
- OpenWeather uses UTC time zone for all API calls.
- You can compare current weather in up to 5 cities at a time. Cities will be sorted from warmest to coldest in the output.

### Instructions:
1. Install 'requests' module. On Windows:
> python -m pip install requests
2. Add your API key to keys.py. To get your API key, go to https://.org. It is FREE, but you need to register.
3. Run main.py file. Enter cities in the following format, i.e.,
   Paris,FR [City,2-letter Country Code]
   Louisville,KY,US [City,2-letter State Code,US] -> for US locations

### File Descriptions
1. main.py. Main file that you need to run.
2. city.py. Holds CityWeather class, class method, and functions needed to print city weather information.
3. keys.py. Add your own OpenWeather API key there.
4. example_output.txt. Example output from console run.

### Notes
This is a simple program created to demonstrate basic knowledge gained through Python CodeLouisville track.

Below is the list of CodeLouisville Python Project Requirements that were fulfilled.
1. Implement a "master loop" console application where the user can repeatedly enter commands/perform actions.
2. Create a class, then create at least one object of that class and populate it with data.
3. Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program.
4. Create and call at least 3 functions or methods, at least one of which must return a value that is used somewhere else in your code.
5. Connect to an external/3rd party API and read data into your app.

**Thank you!** :sun_with_face:
