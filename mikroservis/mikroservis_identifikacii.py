import random
import requests
import json
from datetime import datetime



user = 'demo'#"Svetka"
password = 'demo'#"153759"
url = 'http://vps1:3010/ms' #http://192.168.0.118:889/request    http://192.168.0.135:3010/request
def login():
    i = 0

    while i < 5:
        print(i)

        IP = {"Auth": {"UserName":user,"Password":password},
             "SubSystem":"IP", # IP, FL
             #"Service":"IDUL",
             "Params":{"IDIP" : 1,
                       #"OGRNIP": "312774618000575",
                       #"INNIP": "",
                       "SurName": "ИВАНОВ",
                       "FirstName": "ВЛАДИМИР",
                       "MiddleName": "АЛЕКСАНДРОВИЧ",
                       "RegionExp": "45",
                       }
        }
        IP_sub = str(IP["SubSystem"])

        UL = {"Auth": {"UserName": user, "Password": password},
              "SubSystem": "UL",  # IP, FL
              # "Service":"IDUL",
              "Params": {"IDUL": 1,
                         #"OGRN": "1025900759598",
                         #"INN": "2722016797",
                         "NameOrg": "СТРОЙ",
                         "Address": "45, москва",
                         #"Phone": [""],
                         #"LeaderFIO": "Горлова Елена Николаевна",
                         }
              }
        UL_sub = str(UL["SubSystem"])

        FL = {"Auth": {"UserName": user, "Password": password},
              "SubSystem": "FL",  # IP, FL
              # "Service":"IDUL",
              "Params": {"IDFL": 1,
                         #"OGRNIP": "312774618000575",
                          "SurName": "БУЛАВКИН",
                         "FirstName": "АЛЕКСАНДР",
                         "MiddleName": "СЕРГЕЕВИЧ",
                         "DateOfBirth": "17.03.1961",
                         #"Passport": "4014249174"
                         # "Address": "dasdas",
                         # "Phone": [""],
                         # "LeaderInfo": "Ivanov ivan",
                         }
              }
        FL_sub = str(FL["SubSystem"])


        ran = [IP, UL, FL]



        j = random.choice(ran)

        # ---------------------------------------------------
        #j = IP
        # ---------------------------------------------------


        subsystem = str(j["SubSystem"])
        print(subsystem)
        j=json.JSONEncoder().encode(j)

        HEADERS = {
            'Content-Type': 'application/json;charset=utf-8',
            'Host': "open.croinform.ru:889",
            # 'Connection': 'Keep-Alive',
        }
        r = requests.post(url, data=j, headers=HEADERS, verify=False, )
        #print(r.text)
        parsed_string = r.json()



        try:

            if subsystem == UL_sub:
                #print(parsed_string)
                print('Date: ' + parsed_string['Date'])
                print('Time: ' + parsed_string['Time'])
                print('Response: ' )
                print('NameOrg: ' + parsed_string['Response']['NameOrg'])
                for a in parsed_string['Response']['Answer']:
                    print('INN: ' + a['INN'])
                    print('Address: ' + a['Address'])
                    print('OGRN: ' + a['OGRN'])
                    print('Okved: ' + a['Okved'])
                    print('OkvedCode: ' + a['OkvedCode'])
                    print('Status: ' + a['Status'])
                    print('DateOfReg: ' + a['DateOfReg'])
                    print('DateEnd: ' + a['DateEnd']) #parsed_string['Response']['Answer'][0]['DateEnd'])
                    print('Balance: ' + str(parsed_string['Balance']))
                print('------------------')


            if subsystem == IP_sub:
                # print(parsed_string)
                print('Date: ' + parsed_string['Date'])
                print('Time: ' + parsed_string['Time'])
                print('Response: ')
                for a in parsed_string['Response']['Answer']:
                    print('OGRNIP: ' + a['OGRNIP'])
                    print('INNIP: ' + a['INNIP'])
                    print('Status: ' + a['Status'])
                    print('MiddleName: ' + a['MiddleName'])
                    print('SurName: ' + a['SurName'])
                    print('FirstName: ' + a['FirstName'])
                    print('DateOfReg: ' + a['DateOfReg'])
                    print('Balance: ' + str(parsed_string['Balance']))
                    print('------------------')


            if subsystem == FL_sub:
                #print(parsed_string)
                print('Date: ' + parsed_string['Date'])
                print('Time: ' + parsed_string['Time'])
                print('Response: ')
                for a in parsed_string['Response']['Answer']:
                    print('MiddleName: ' + a['MiddleName'])
                    print('SurName: ' + a['SurName'])
                    print('FirstName: ' + a['FirstName'])
                    print('NameOrg: ' + str(a['NameOrg']))
                    print('Phone: ' + str(a['Phone']))
                    print('Passport: ' + str(a['Passport']))
                    print('Address: ' + str(a['Address']))
                    print('negativeResult: ' + str(a['negativeResult']))
                    print('Balance: ' + str(parsed_string['Balance']))
                print('------------------')


        except:
            print(parsed_string)

        i+=1




start_time = datetime.now()
login()
end_time = datetime.now()
total_time = end_time - start_time
print(total_time)