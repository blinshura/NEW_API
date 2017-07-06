
from bs4 import BeautifulSoup
from grab import *
import json



g = Grab( follow_location= True,reuse_cookies=True, follow_refresh=True, timeout=1000, connect_timeout=30, debug_post=True, encoding='')

def login():

    j = {"Auth": {"UserName":"tester001","Password":"001"},
         "SubSystem":"UL", # IP, FL
         #"Service":"IDUL",
         "Params":{"IDUL" : 1,
                    #"OGRN": "5077746887312",
                   #"INN": "",
                   #"INNIP": "",
                   #"OGRNIP": "",
                   "NameOrg": "ООО ромашка",
                   "Address": "dasdas",
                   #"Phone": [""],
                    "LeaderInfo": "Ivanov ivan",
                   }
    }



    j=json.JSONEncoder().encode(j)
    #j=json.dumps(j)

    g.setup(post=j ,
            headers= {
                'Content-Type': 'application/json;charset=utf-8',
                'Host': "ips1:889",
                'Connection': 'Keep-Alive',
                }
            )
    g.go('http://192.168.0.118:889/request')
    xmlBODY = g.response.body
    soup = BeautifulSoup(xmlBODY, 'lxml')
    print(soup)




login()