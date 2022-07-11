import requests
import json
import io

f = open('api_key.txt','r')
API_KEY = f.read()

f.close()


URL = 'https://developer-api.govee.com/v1/devices/control'
HEADERS = {'Govee-API-Key' : API_KEY, 'content-type': 'application/json'}
DATA = {
    'device': 'BB:D3:A4:C1:38:47:77:C2',
    'model': 'H6110',
    'cmd': {
	'name': 'turn',
	'value': 'on'
}
}
r = requests.put(URL,headers=HEADERS,data=json.dumps(DATA))

#data = r.json()
print(r)
print(r.content)