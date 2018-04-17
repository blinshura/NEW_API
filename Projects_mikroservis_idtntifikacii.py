import random
from bs4 import BeautifulSoup
from grab import *
import json
from datetime import datetime

g = Grab( follow_location= True,reuse_cookies=True, follow_refresh=True, timeout=1000, connect_timeout=30, debug_post=True, encoding='')
user = "release"
password = "release"
url = ('http://192.168.0.135:3010/request') #http://192.168.0.118:889/request    http://192.168.0.135:3010/request
def login():
    i = 0

    while i < 5:
        print(i)

        IP = {"Auth": {"UserName":user,"Password":password},
             "SubSystem":"IP", # IP, FL
             #"Service":"IDUL",
             "Params":{"IDIP" : 1,
                       "OGRNIP": "312774618000575",
                       #"INNIP": "",
                       #"NameOrg": "romashka",
                       "Address": "dasdas",
                       #"Phone": [""],
                       #"LeaderInfo": "Ivanov ivan",
                       }
        }
        IP_sub = str(IP["SubSystem"])

        UL = {"Auth": {"UserName": user, "Password": password},
              "SubSystem": "UL",  # IP, FL
              # "Service":"IDUL",
              "Params": {"IDUL": 1,
                         #"OGRN": "1044217029471",
                         #"INN": "2722016797",
                         "NameOrg": "ООО МОДУЛЬ",
                         "Address": "01 БАРНАУЛ ПАРТИЗАНСКАЯ 266",
                         #"Phone": [""],
                         #"LeaderFIO": "Уваров Вадим Валерьянович",
                         }
              }
        UL_sub = str(UL["SubSystem"])

        FL = {"Auth": {"UserName": user, "Password": password},
              "SubSystem": "FL",  # IP, FL
              # "Service":"IDUL",
              "Params": {"IDFL": 1,
                         "OGRNIP": "312774618000575",
                         # "SurName": "БУЛАВКИН",
                         # "FirstName": "АЛЕКСАНДР",
                         # "MiddleName": "СЕРГЕЕВИЧ",
                          #"DateOfBirth": "17.03.1961",
                         # "Address": "dasdas",
                         # "Phone": [""],
                         #"INNIP": "861005775557",
                         # "Seria": "4507",
                         # "Number": "330202"
                         }
              }
        FL_sub = str(FL["SubSystem"])


        ran = [IP, UL, FL]



        j = random.choice(ran)

        #---------------------------------------------------
        j = FL
        #---------------------------------------------------

        print(j["SubSystem"])
        subsystem = str(j["SubSystem"])


        j=json.JSONEncoder().encode(j)
        #j=json.dumps(j)

        g.setup(post=j ,
                headers= {
                    'Content-Type': 'application/json;charset=utf-8',
                    'Host': "vips1",
                    #'Connection': 'Keep-Alive',
                    }
                )
        g.go(url) #http://192.168.0.118:889/request    http://192.168.0.135:3010/request
        xmlBODY = g.doc.body
        soup = BeautifulSoup(xmlBODY, 'lxml')
        #print(soup.prettify())

        str_soup = str(soup)
        json_string = str_soup[15:-18]
        print(json_string)
        parsed_string = json.loads(json_string)

        try:

            if subsystem == UL_sub:
                # print(parsed_string)
                print('Date: ' + parsed_string['Date'])
                print('Time: ' + parsed_string['Time'])
                print('Response: ')
                print('NameOrg: ' + parsed_string['Response']['NameOrg'])
                for u in parsed_string['Response']['Answer']:
                    print('INN: ' + u['INN'])
                    print('Address: ' + u['Address'])
                    print('OGRN: ' + u['OGRN'])
                    print('Okved: ' + u['Okved'])
                    print('OkvedCode: ' + u['OkvedCode'])
                    print('Status: ' + u['Status'])
                    print('DateOfReg: ' + u['DateOfReg'])
                    print('DateEnd: ' + u['DateEnd'])  # parsed_string['Response']['Answer'][0]['DateEnd'])
                    print('Balance: ' + str(parsed_string['Balance']))
                print('------------------')

            if subsystem == IP_sub:
                # print(parsed_string)
                print('Date: ' + parsed_string['Date'])
                print('Time: ' + parsed_string['Time'])
                print('Response: ')
                print('OGRNIP: ' + parsed_string['Response']['OGRNIP'])
                print('INNIP: ' + parsed_string['Response']['INNIP'])
                print('Status: ' + parsed_string['Response']['Status'])
                print('MiddleName: ' + parsed_string['Response']['MiddleName'])
                print('SurName: ' + parsed_string['Response']['SurName'])
                print('FirstName: ' + parsed_string['Response']['FirstName'])
                print('DateOfReg: ' + parsed_string['Response']['DateOfReg'])
                print('Balance: ' + str(parsed_string['Balance']))
                print('------------------')

            if subsystem == FL_sub:
                for a in parsed_string['Response']['Answer']:
                    print('SurName: ' + str(a['SurName']))
                    print('FirstName: ' + str(a['FirstName']))
                    print('MiddleName: ' + str(a['MiddleName']))
                    print('DateOfBirth: ' + str(a['DateOfBirth']))
                    print('INN: ' + str(a['INN']))
                    print('Passport: ' + str(a['Passport']))
                    print('OGRN: ' + str(a['OGRN']))
                    print('Address: ' + str(a['Address']))
                    print('negativeResult: ' + str(a['negativeResult']))





        except:
            print(parsed_string)

        i+=1




start_time = datetime.now()
login()
end_time = datetime.now()
total_time = end_time - start_time
print(total_time)