"""
My personal yahoo weather report with python 3.

yql queries examples:
"select wind from weather.forecast where woeid=2460286"
'select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="nome, ak")'
'select item.condition from weather.forecast where woeid = 2487889'

yahoo ressources:
https://developer.yahoo.com
https://developer.yahoo.com/oauth2/guide/
https://developer.yahoo.com/attribution/
https://developer.yahoo.com/weather/#ratelimits

python ressources
https://docs.python.org/3/library/urllib.parse
"""
import json
import os
import urllib.parse
import urllib.request
from pprint import pprint

woeid = os.environ['WOEID']
baseurl = "https://query.yahooapis.com/v1/public/yql?"
forecast = 'select * from weather.forecast where woeid = ' + woeid
conditions = 'select item.condition from weather.forecast where woeid = ' + woeid

yql_url = baseurl + urllib.parse.urlencode({'q': forecast}) + "&format=json"


def get_data(url):
    # Takes a url and return json data

    with urllib.request.urlopen(url) as response:
        r = response.read()
        data = json.loads(r.decode('utf-8'))
    return data


data = get_data(yql_url)
pprint(data['query']['results'])
