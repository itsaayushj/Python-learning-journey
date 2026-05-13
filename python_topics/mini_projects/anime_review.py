import requests

base_url = "https://api.jikan.moe/v4/"
end_url = "anime?="
searched_anime = input("Enter the anime you are searching for: ")
response = requests.get(f"{base_url}{end_url}{searched_anime}")
data = response.json()
print(data)
