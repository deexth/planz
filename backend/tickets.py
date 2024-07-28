import requests
from requests.exceptions import HTTPError
from dotenv import load_dotenv
import os

from pydantic import BaseModel

load_dotenv()

KIWI = os.getenv("KIWI_API")
URL = "https://api.tequila.kiwi.com/"

headers = {
    "Content-Type": "application/json",
    "apikey": KIWI,
    "Content-Enconding": "gzip",
}

# class LocCodes(BaseModel):
#     codes: dict

# class Loc(BaseModel):
#     departure: str
#     arrival: str
#     LOC_TYPE: str = 'city'


def get_loc(location) -> dict:
    params = {
        "term": location,
        "locale": "en-US",
        "location_types": "city",
        "limit": 10,
        "active_only": True,
    }

    try:
        response = requests.get(
            URL + "locations/query", headers=headers, params=params, timeout=5
        )
        response.raise_for_status()
    except HTTPError as http_err:
        return f"HTTP error occured: {http_err}"
    except Exception as err:
        return f"This error occired: {err}"
    
    response_dict = response.json()

    return {"location": response_dict["locations"][0]["code"]}


def get_ticket() -> str:
    params = {
        "fly_from": ...,
        "fly_to": ...,
        "date_from": ...,
        "date_to": ...,
        "return_from": ...,
        "return_to": ...,
        "nights_in_dst_from": ...,
        "nights_in_dst_to": ...,
        "max_fly_duration": ...,
        "ret_from_diff_city": ...,
        "ret_to_diff_city": ...,
        "adults": ...,
        "selected_cabins": ...,
        "adult_hold_bag": ...,
        "adult_hand_bag": ...,
        "stopover_to": ...,
        "max_stopovers": ...,
        "ret_from_diff_airport": ...,
        "ret_to_diff_airport": ...,
    }
    try:
        response = requests.get(URL + "v2/search", headers=headers, params=params, timeout=5)
        response.raise_for_status()
    except HTTPError as http_err:
        return f"HTTP error occured: {http_err}"
    except Exception as err:
        return f"This error occired: {err}"
    
    response_dict = response.json()
    
    return {"Ticke": response_dict}
