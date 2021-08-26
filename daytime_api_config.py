import os
import requests
from datetime import datetime
from data import *

def is_night():
    parameters = {
        "lat": WROCLAW_LATITUDE,
        "lng": WROCLAW_LONGITUDE,
        "formatted": 0,
    }

    sunrise_sunset_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    sunrise_sunset_response.raise_for_status()
    json_data = sunrise_sunset_response.json()
    sunrise = int(json_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(json_data["results"]["sunset"].split("T")[1].split(":")[0])
    current_time = datetime.now().hour

    if current_time >= sunset or current_time <= sunrise:
        return True
