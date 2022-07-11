import requests
import json

URL = 'https://developer-api.govee.com/v1/devices'
HEADERS = {'Govee-API-Key' : '6a43de81-80b9-4a68-8fb6-3fedead8421c'}
DATA = {
    'device':'BB:D3:A4:C1:38:47:77:C2',
    'model':'H6110',
    'cmd':{
        'name':'turn',
        'value':'on'
    }
}
r = requests.put(URL,headers=HEADERS,data=DATA)

#data = r.json()
#print(r.text)