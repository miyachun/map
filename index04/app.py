import requests
import pandas as pd
import json,urllib.request
#25.047846496934394, 121.51740617725997
#zh-TW
api_key = 'XXXXX'

category_response = requests.get(f'https://api.tomtom.com/search/2/nearbySearch/.json?lat=25.047846496934394&lon=121.51740617725997&limit=5&radius=10000&language=zh-TW&categorySet=7315&view=Unified&relatedPois=off&key={api_key}')
category_data = category_response.json()


with open('data.json', 'w') as f:
    json.dump(category_data, f)


f = open('data.json')
dataf = json.load(f)
print(dataf)
