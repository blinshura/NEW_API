import json
import requests



STATUSbug = []
url = 'http://portal14:8826'


with open("VI_IP_data.txt", 'r', encoding='utf-8') as f:
    for i,line in enumerate(f):
        No = line.split(';')[0]
        INN = line.split(';')[1]
        inOut = line.split(';')[2]
        sourceName = line.split(';')[3]
        OGRNIP = line.split(';')[4]
        Seria = line.split(';')[5]
        Number = str(line.split(';')[6])
        SurName = line.split(';')[7]
        FirstName = line.split(';')[8]
        MiddleName = line.split(';')[9]
        PhoneExp = line.split(';')[10]
        RegionExp = line.split(';')[11]
        CityExp = line.split(';')[12]
        StreetExp = line.split(';')[13]
        HouseExp = line.split(';')[14]
        DateOfBirth = line.split(';')[15]
        RegistredIP = line.split(';')[16]

        # print("line {0} = {1}".format(i,line.split(';')))

        if inOut == 'Внутренний' and sourceName != '-':
            data = {
                "source": sourceName,
                "number": No,
                "INNIP": INN,
                "OGRNIP": OGRNIP,
                "Seria": Seria,
                "Number":Number,
                "SurName":SurName,
                "FirstName":FirstName,
                "MiddleName":MiddleName,
                "PhoneExp":PhoneExp,
                "RegionExp":RegionExp,
                "CityExp":CityExp,
                "StreetExp":StreetExp,
                "HouseExp":HouseExp,
                "DateOfBirth":DateOfBirth,
                "RegistredIP":RegistredIP,

                    }





            jdata = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False).encode('utf-8')
            r = requests.post(url, data=jdata)
            #print(r.text)


            try:
                if r.json():
                    if (str(r.json()['status'])) == '1':
                        print(str(data['number']) + '   ' + str(data['source']) + ' : ' + str(r.json()['status']))
                    else:
                        bug = str(data['number']) + '   ' + str(data['source']) + ' : ' + str(r.json()['status'])
                        print('BUG - ' + bug)
                        STATUSbug.append(bug)
                else:
                    print(str(str(data['number']) + '   ' + data['source']) + ' : ' + '\n' + r.text)
            except Exception as e:
                Ex = str('Exception : ' + str((data['number']) + '   ' + data['source']))
                print(Ex)
                print(str(e) + '\n')
                print(r.text)
                STATUSbug.append(Ex)

        print('---------------------------------------------------------------------------------------------------------')


print('TEST END ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ TEST END')
print('BUGS:')
for i in STATUSbug:
    print(i)