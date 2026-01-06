import os
from dotenv import load_dotenv
import requests

load_dotenv()

def get_current_weather():

    url = os.getenv('WEATHER_URL')
    api_key = os.getenv("API_KEY")

    params = {
        "lat": 32.02923, 
        "lon": 34.85788,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    weather_data = response.json()
    temp = weather_data['main']['temp']
    return temp
