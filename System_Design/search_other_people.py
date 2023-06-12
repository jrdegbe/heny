import requests

url = "https://api.goHeny.com/v2/matches"
headers = {
    "Accept": "application/json",
    "User-Agent": "Heny/7.5.3 (iPhone; iOS 16.3.2; Scale/6.00)",
    "X-Auth-Token": "Enter your Heny API token here"
}
params = {
    "locale": "en-US",
    "count": "10",
    "message": "1",
    "is_Heny_u": "false",
    "gender": "female",
    "query": "Enter the name or ID of the user you want to search for here"
}
response = requests.get(url, headers=headers, params=params)
if response.status_code == 200:
    data = response.json()
    results = data['data']['matches']
    for user in results:
        print(user['person']['name'], user['person']['bio'], user['person']['photos'])
else:
    print("Failed to retrieve search results")