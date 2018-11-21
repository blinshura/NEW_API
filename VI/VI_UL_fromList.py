import json
import requests



STATUSbug = []
url = 'http://portal14:8826'


with open("VI_UL_data.txt", 'r', encoding='utf-8') as f:
    for i,line in enumerate(f):
        No = line.split(';')[0]
        INN = line.split(';')[1]
        inOut = line.split(';')[2]
        sourceName = line.split(';')[3]
        DataForVI = json.loads(line.split(';')[4])
        masAddress = json.loads(line.split(';')[5])
        ogrnUL = str(line.split(';')[6])
        masNameUL = line.split(';')[7]
        longnameUL = line.split(';')[8]
        # print("line {0} = {1}".format(i,line.split(';')))

        if inOut == 'Внутренний' and sourceName != '-':
            data = {"innUL": INN,
                     "source": sourceName,
                     "number": No,
                    "DataForVI": DataForVI,
                    "masAddress": masAddress,
                    "ogrnUL": ogrnUL,
                    "masNameUL": masNameUL,
                    "longnameUL": longnameUL
                    }



            jdata = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False).encode('utf-8')
            r = requests.post(url, data=jdata)


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