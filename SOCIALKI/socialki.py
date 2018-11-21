import requests
import json


# from API import API_parrent as ap
# ap()


url = 'http://portal6:3000'
STATUSbug = []
r = requests
HEADERS = {'Content-Type': 'application/json;charset=utf-8'}

password = "jztJxSL0Z9l2STHKwScz"
userName = "cronos"

DATA = [
    {"LastName": "ПОЖИЛЕНКО",
     "FirstName": "ЕВГЕНИЙ",
     "MaidenName": "АНДРЕЕВИЧ",
     "BirthDate": "16.10.1984",
     "UserName": userName,
     "Password": password
     },


]



try:
    # for i in DATA:
    #     data = i
    #     jdata= json.JSONEncoder().encode(data)
    #     r = r.post(url, data=jdata)
    #     if r.json():
    #         print(str(data['source']) + ' : ' + str(r.json()['status']))
    #         if (str(r.json()['status'])) != '1':
    #             bug = str(data['source']) + ' : ' + str(r.json()['status'])
    #             STATUSbug.append(bug)



    data = DATA[0]
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
    jdata = json.JSONEncoder().encode(data)
    print('--------------------')
    r = r.post(url, data=jdata, headers=HEADERS)
    parsed = json.dumps(r.json(), indent=4, sort_keys=True, ensure_ascii=False)
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print(parsed)
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

except:
    print(r.text)

print('\n')
print('test end ====================================================== test end' + '\n')


print('bugs:')
for i in STATUSbug:
    print(i)