import json
import requests

URL = 'http://portal14:4500' #192.168.0.73
HEADERS={'Content-Type': 'application/json; charset=utf-8'}
post = {
"SubSystem": "MS",
"Service": "Address",
"Params" : {
    "Address" : "МОСКВА Проезд Сокольнического Круга 1 ",
    "FullAddress" : {
            "Region" : "",
            "City" : "",
            "Street" : "",
            "House" : "",
            "Build" : "",
            "Flat" : ""}
            }
    }
post = json.dumps(post, ensure_ascii=False).encode('utf8')
r = requests.post(URL, data=post, headers=HEADERS, verify=False)

# print(r.content)
answer = r.json()


print(answer['Response']['Answer'])

