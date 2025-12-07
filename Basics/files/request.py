import requests

r = requests.get('https://google.com',verify=False)
print(r.status_code)
print(r.text)  