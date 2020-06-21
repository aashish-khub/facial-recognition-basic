import requests
import pandas
import numpy
import json

url = "http://api.followthemoney.org/?dt=1&c-t-eid=9284790,15203357&gro=c-t-id&APIKey=47b851822558e72e4c3404484218bfff&mode=json"

response = requests.get(url)



def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())
