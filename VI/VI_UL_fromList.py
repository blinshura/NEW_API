import json
import requests



STATUSbug = []
url = 'http://portal14:8826'
s = requests.session()

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
            r = s.post(url, data=jdata)
            statusFirstChar = r.text.find('"status":')
            status = r.text[statusFirstChar + 9]



            try:
                # if ((r.text)[:11]+'}') == '{"status":1}' or '{"status":2}' or '{"status":3}' or '{"status":4}':
                #     status = json.loads((r.text)[:11]+'}')
                # else:
                #     status['status'] = "разгребай ответ руками"

                if status == '1' or status == '2' or status == '3' or status == '4':
                    if INN != '7811143861':
                        if status == '1':
                            print(str(data['number']) + '   ' + str(data['source']) + ' : ' + str(status))
                        else:
                            bug = str(data['number']) + '   ' + str(data['source']) + ' : ' + str(status)
                            print('BUG - ' + bug)
                            STATUSbug.append(bug)


                    if INN == '7811143861':
                        if status == '2':
                            print(str(data['number']) + '   ' + str(data['source']) + ' : ' + str(status))
                        else:
                            bug = str(data['number']) + '   ' + str(data['source']) + ' : ' + str(status)
                            print('BUG - ' + bug)
                            STATUSbug.append(bug)

                else:
                    print((str(data['number']) + '   ' + data['source']) + ' : ' + '\n' + r.text)
                    bug = str(data['number']) + '   ' + str(data['source']) + ' : ' + str(status)
                    print('BUG - ' + bug)
                    STATUSbug.append(bug)



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

print('UL test end=========================================================================' + '\n')