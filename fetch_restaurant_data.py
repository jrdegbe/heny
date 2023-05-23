import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YELP_API_KEY")

def fetch_restaurant_data(location):
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    params = {
        "term": "restaurants",
        "location": location,
        "limit": 50
    }
    response = requests.get("https://api.yelp.com/v3/businesses/search", headers=headers, params=params)
    data = response.json()
    return data["businesses"]

if __name__ == "__main__":
    restaurants = fetch_restaurant_data("New York City")
    print(restaurants)

