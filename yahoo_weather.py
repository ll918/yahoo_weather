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
# language = weather_data['language']
# lastBuildDate = weather_data['lastBuildDate']
# link = weather_data['link']
pprint(weather_data)

title = weather_data['title']

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

location = weather_data['location']
city = location['city']
country = location['country']
region = location['region']  # province

item = weather_data['item']
description_html = item['description']
link = item['link']
lat = item['lat']
long = item['long']
item_pubDate = item['pubDate']
item_title = item['title']

condition = item['condition']
condition_code = condition['code']
condition_date = condition['date']
condition_temp = condition['temp']
condition_text = condition['text']

# list of dict. keys: date, day, text, high, low, code
forecast = item['forecast']

units = weather_data['units']
distance_unit = units['distance']
pressure_unit = units['pressure']
speed_unit = units['speed']
temperature_unit = units['temperature']

wind = weather_data['wind']
wind_speed = wind['speed']
wind_direction = wind['direction']  # degrees
