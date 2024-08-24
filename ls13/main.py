import requests

resp = requests.get('https://dummyjson.com/products')
print(resp.json())