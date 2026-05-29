import requests

NOAA_URL = "https://services.swpc.noaa.gov/json/planetary_k_index_1m.json"

def get_kp_index():
    response = requests.get(NOAA_URL, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data[-1]
