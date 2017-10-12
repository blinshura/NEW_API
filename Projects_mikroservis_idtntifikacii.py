import random
from bs4 import BeautifulSoup
from grab import *
import json
from datetime import datetime

g = Grab( follow_location= True,reuse_cookies=True, follow_refresh=True, timeout=1000, connect_timeout=30, debug_post=True, encoding='')
user = "nbki"
password = "nbki"
url = ('http://192.168.0.118:889/request') #http://192.168.0.118:889/request    http://192.168.0.135:3010/request
def login():
    i = 0

    while i < 1:
        print(i)

        IP = {"Auth": {"UserName":user,"Password":password},
             "SubSystem":"IP", # IP, FL
             #"Service":"IDUL",
             "Params":{"IDIP" : 1,
                       "OGRNIP": "312774618000575",
                       #"INN": "",
                       #"INNIP": "",
                       #"OGRNIP": "",
                       #"NameOrg": "romashka",
                       #"Address": "dasdas",
                       #"Phone": [""],
                       #"LeaderInfo": "Ivanov ivan",
                       }
        }

        UL = {"Auth": {"UserName": user, "Password": password},
              "SubSystem": "UL",  # IP, FL
              # "Service":"IDUL",
              "Params": {"IDUL": 1,
                         #"OGRN": "1044217029471",
                         #"INN": "2722016797",
                         "NameOrg": "ООО МОДУЛЬ",
                         "Address": "01 БАРНАУЛ",
                         #"Phone": [""],
                         #"LeaderInfo": "Уваров Вадим Валерьянович",
                         }
              }

        FL = {"Auth": {"UserName": user, "Password": password},
              "SubSystem": "FL",  # IP, FL
              # "Service":"IDUL",
              "Params": {"IDFL": 1,
                         #"OGRNIP": "312774618000575",
                          "INN": "501002007286",
                         # "INNIP": "",
                         # "OGRNIP": "",
                         # "NameOrg": "romashka",
                         # "Address": "dasdas",
                         # "Phone": [""],
                         # "LeaderInfo": "Ivanov ivan",
                         }
              }


        ran = [IP, UL, ]



        j = random.choice(ran)
        j = UL
        print(j["SubSystem"])

        j=json.JSONEncoder().encode(j)
        #j=json.dumps(j)

        g.setup(post=j ,
                headers= {
                    'Content-Type': 'application/json;charset=utf-8',
                    'Host': "open.croinform.ru:889",
                    #'Connection': 'Keep-Alive',
                    }
                )
        g.go(url) #http://192.168.0.118:889/request    http://192.168.0.135:3010/request
        xmlBODY = g.response.body
        soup = BeautifulSoup(xmlBODY, 'lxml')
        #print(soup.prettify())

        str_soup = str(soup)
        json_string = str_soup[15:-18]
        print(json_string)
        parsed_string = json.loads(json_string)

        for a in parsed_string['Response']['Answer']:
            print(a)

        print('------------------')

        i+=1




start_time = datetime.now()
login()
end_time = datetime.now()
total_time = end_time - start_time
print(total_time)