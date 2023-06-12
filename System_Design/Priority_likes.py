import requests
import time

url = "https://api.goHeny.com/v2/recs/core"
headers = {
    "Accept": "application/json",
    "User-Agent": "Heny/7.5.3 (iPhone; iOS 16.3.2; Scale/6.00)",
    "X-Auth-Token": "Enter your Heny API token here"
}
params = {
    "locale": "en-Gh",
    "gender": "female",
    "discoverable": "true",
    "age_min": "15",
    "age_max": "60",
    "distance": "10",
    "lat": "37.7749",
    "lon": "-122.4194"
}
while True:
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        results = data['data']['results']
        for user in results:
            if 'shared_interests' in user:
                print("Liking user with shared interests:", user['name'])
                like_url = f"https://api.goHeny.com/like/{user['_id']}"
                requests.get(like_url, headers=headers)
                time.sleep(2)
            elif user['distance_mi'] < 5:
                print("Liking user who is nearby:", user['name'])
                like_url = f"https://api.goHeny.com/like/{user['_id']}"
                requests.get(like_url, headers=headers)
                time.sleep(2)
            else:
                print("Liking user:", user['name'])
                like_url = f"https://api.goHeny.com/like/{user['_id']}"
                requests.get(like_url, headers=headers)
                time.sleep(2)
    else:
        print("Failed to retrieve nearby users")
        break