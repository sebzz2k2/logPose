import requests
from core.constants import Constants

def get_country():
    try:
        response = requests.get("https://ipinfo.io", timeout=5)
        data = response.json()
        return data.get("country") or Constants.DEFAULT_COUNTRY.value
    except Exception as e:
        # Log the exception 
        return Constants.DEFAULT_COUNTRY.value
