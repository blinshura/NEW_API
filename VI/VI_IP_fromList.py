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

        if sourceName != '-':
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
            if inOut == 'Внешний':
                url = 'http://ves1:8827'
            else:
                url = 'http://portal14:8826'


            print("URL: " + url + " src " + sourceName)
            jdata = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False).encode('utf-8')



            try:
                r = requests.post(url, data=jdata, timeout=70)
                statusFirstChar = r.text.find('"status":')
                status = r.text[statusFirstChar + 9]
                # print(r.text)
                # if ((r.text)[:11]+'}') == '{"status":1}' or '{"status":2}' or '{"status":3}' or '{"status":4}':
                #     status = json.loads((r.text)[:11]+'}')
                # else:
                #     status['status'] = "разгребай ответ руками"

                if status == '1' or status == '2' or status == '3' or status == '4':
                    if INN != '200818124592':
                        if status == '1':
                            print(str(data['number']) + '   ' + str(data['source']) + ' : ' + str(status) + "   URL: " + url)
                        else:
                            bug = str(data['number']) + '   ' + str(data['source']) + ' : ' + str(status) + "   URL: " + url
                            print('BUG - ' + bug)
                            STATUSbug.append(bug)


                    if INN == '200818124592':
                        if status == '2':
                            print(str(data['number']) + '   ' + str(data['source']) + ' : ' + str(status) + "   URL: " + url)
                        else:
                            bug = str(data['number']) + '   ' + str(data['source']) + ' : ' + str(status) + "   URL: " + url
                            print('BUG - ' + bug)
                            STATUSbug.append(bug)

                else:
                    print((str(data['number']) + '   ' + data['source']) + ' : ' + '\n' + r.text)
                    bug = str(data['number']) + '   ' + str(data['source']) + ' : ' + str(status) + "   URL: " + url
                    print('BUG - ' + bug)
                    STATUSbug.append(bug)


            except Exception as e:
                Ex = str('Exception : ' + str(e) + '    ' + str((data['number']) + '   ' + data['source']) + "  URL: " + url)
                print(Ex)
                STATUSbug.append(Ex)

        print('---------------------------------------------------------------------------------------------------------')


print('TEST END ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ TEST END')
print('BUGS:')
for i in STATUSbug:
    print(i)

print('IP test end=========================================================================' + '\n')