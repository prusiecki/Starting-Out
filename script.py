import requests

r = requests.get("https://cmcmarkets.com")

print(r.status_code)
print(r.ok)
#come n