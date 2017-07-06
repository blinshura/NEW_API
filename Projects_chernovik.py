import json
import urllib3.request

import urllib.request
import json

body = {
                    "Auth": {
                    "UserName":"danis",
                    "Password":"123"
                    },
                    "SubSystem": "IP",
                    "Service": "IDFL",
                    "Params": {
                    "INNIP": "320500822345"
                    }
                    }

myurl = "http://80.78.250.34:80"
req = urllib.request.Request(myurl)
req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps(body)
jsondataasbytes = jsondata.encode('utf-8')  # needs to be bytes
req.add_header('Content-Length', len(jsondataasbytes))
print(jsondataasbytes)
response = urllib.request.urlopen(req, jsondataasbytes)

