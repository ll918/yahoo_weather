"""
My personal yahoo weather report with python 3.

https://developer.yahoo.com/weather/documentation.html

yql queries examples:
"select wind from weather.forecast where woeid=2460286"
'select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="nome, ak")'
'select item.condition from weather.forecast where woeid = 2487889'

yahoo ressources:
https://developer.yahoo.com
https://developer.yahoo.com/weather/
https://developer.yahoo.com/oauth2/guide/
https://developer.yahoo.com/attribution/
https://developer.yahoo.com/weather/#ratelimits

http://www.woeidlookup.com/

python ressources
https://docs.python.org/3/library/urllib.parse

Notes:
    add 'and u = "c"' to query for metric data
"""
import json
import os
import urllib.parse
import urllib.request
from pprint import pprint

woeid = os.environ['WOEID']
baseurl = "https://query.yahooapis.com/v1/public/yql?"
forecast_query = 'select * from weather.forecast where woeid = ' + woeid + 'and u = "c"'
conditions_query = 'select item.condition from weather.forecast where woeid = ' + woeid + 'and u = "c"'

yql_url = baseurl + urllib.parse.urlencode(
    {'q': forecast_query}) + "&format=json"


def get_data(url):
    # Takes a url and return json data

    with urllib.request.urlopen(url) as response:
        r = response.read()
        json_data = json.loads(r.decode('utf-8'))
    return json_data


data = get_data(yql_url)
weather_data = data['query']['results']['channel']
pprint(weather_data)

astronomy = weather_data['astronomy']
sunrise = astronomy['sunrise']
sunset = astronomy['sunset']

atmosphere = weather_data['atmosphere']
humidity = atmosphere['humidity']
pressure = atmosphere['pressure']
rising = atmosphere['rising']
visibility = atmosphere['visibility']

description = weather_data['description']

# weather_data['image']

item = weather_data['item']
condition = item['condition']

######

# language = weather_data['language']
# lastBuildDate = weather_data['lastBuildDate']
# link = weather_data['link']

location = weather_data['location']
city = location['city']
country = location['country']
region = location['region']  # province

title = weather_data['title']

units = weather_data['units']
distance_unit = units['distance']
pressure_unit = units['pressure']
speed_unit = units['speed']
temperature_unit = units['temperature']

wind = weather_data['wind']
speed = wind['speed']
direction = wind['direction']  # degrees
