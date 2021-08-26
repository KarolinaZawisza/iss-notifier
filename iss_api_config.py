import requests
from data import *

def checking_iss_position():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    json_data = iss_response.json()

    iss_latitude = float(json_data["iss_position"]["latitude"])
    iss_longitude = float(json_data["iss_position"]["longitude"])

    if WROCLAW_LONGITUDE-5 <= iss_longitude <= WROCLAW_LONGITUDE+5 \
            and WROCLAW_LATITUDE-5 <= iss_latitude <= WROCLAW_LATITUDE:
        return True
