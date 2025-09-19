import requests

url = "https://catfact.ninja/fact"
response = requests.get(url)
data = response.json()

print("Full JSON:", data)
print("Cat Fact:", data["fact"])
