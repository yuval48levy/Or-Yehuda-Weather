import os
import requests
from weather import get_current_weather

def test_get_current_weather():

    temp = get_current_weather()

    assert isinstance(temp, float)

def test_wrong_api_key():
    url = os.getenv('WEATHER_URL') 
    params = {
        "lat": 32.02923, 
        "lon": 34.85788,
        "appid": 'aaaa',  
        "units": "metric"
    }

    response = requests.get(url, params=params)

    assert response.status_code == 401
