import requests

url = "https://api.goheny.com/v2/recs/core"
headers = {
    "Accept": "application/json",
    "User-Agent": "Heny/7.5.3 (iPhone; iOS 16.3.2; Scale/6.00)",
    "X-Auth-Token": "Enter your heny API token here"
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
response = requests.get(url, headers=headers, params=params)
if response.status_code == 200:
    data = response.json()
    results = data['data']['results']
    for user in results:
        print(user['name'], user['distance_mi'], user['bio'])
else:
    print("Failed to retrieve nearby places")