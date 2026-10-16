import requests
from src.config import API_URL
import os 
def fetch_population(country,api_key):
    headers = {
        "X-Api-Key":api_key
    }
    params = {
        "country":country
    }
    responses = requests.get(API_URL,headers=headers,params=params)
    print("Status code:", responses.status_code)
    print("Response body:", responses.text)

    responses.raise_for_status()
    return responses.json()
