import json
import requests



STATUSbug = []
url = 'http://portal14:8826'


with open("VI_FL_data.txt", 'r', encoding='utf-8') as f:
    for i,line in enumerate(f):
        No = line.split(';')[0]
        inOut = line.split(';')[1]
        sourceName = line.split(';')[2]
        SurName = line.split(';')[3]
        FirstName = str(line.split(';')[4])
        MiddleName = line.split(';')[5]
        DateOfBirth = line.split(';')[6]
        Seria = line.split(';')[7]
        Number = line.split(';')[8]
        INNExp = line.split(';')[9]
        RegionExp = line.split(';')[10]
        RegionExpTmp = line.split(';')[11]
        IssueDate = line.split(';')[12]


        # print("line {0} = {1}".format(i,line.split(';')))

        if inOut == 'Внутренний' and sourceName != '-':
            data = {
                "source": sourceName,
                "number": No,
                "SurName": SurName,
                "FirstName": FirstName,
                "MiddleName": MiddleName,
                "DateOfBirth":DateOfBirth,
                "Seria":Seria,
                "Number":Number,
                "INNExp":INNExp,
                "RegionExp":RegionExp,
                "RegionExpTmp":RegionExpTmp,
                "IssueDate":IssueDate,
                    }





            jdata = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False).encode('utf-8')
            r = requests.post(url, data=jdata)
            statusFirstChar = r.text.find('"status":')
            status = r.text[statusFirstChar + 9]
            #print(r.text)


            try:
                # if ((r.text)[:11]+'}') == '{"status":1}' or '{"status":2}' or '{"status":3}' or '{"status":4}':
                #     status = json.loads((r.text)[:11]+'}')
                # else:
                #     status['status'] = "разгребай ответ руками"

                if status == '1' or status == '2' or status == '3' or status == '4':
                    if INNExp != '200818124592':
                        if status == '1':
                            print(str(data['number']) + '   ' + str(data['source']) + ' : ' + str(status))
                        else:
                            bug = str(data['number']) + '   ' + str(data['source']) + ' : ' + str(status)
                            print('BUG - ' + bug)
                            STATUSbug.append(bug)


                    if INNExp == '200818124592':
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

print('FL test end=========================================================================' + '\n')