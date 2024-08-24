import requests

resp = requests.get('https://fakestoreapiserver.reactbd.com/smart')
print(resp.json())