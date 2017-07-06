from datetime import datetime, time
import re
from bs4 import BeautifulSoup
from grab import *
from lxml import html
import threading
from time import sleep

ID_list = []


Exceptions = []
g = Grab( follow_location= True,reuse_cookies=True, follow_refresh=True, timeout=1000, connect_timeout=30)

def login():

    g.go('http://192.168.0.23:81')
    g.doc.set_input('Name', 'Test_61959959')
    g.doc.set_input('Password', '5253325')
    g.doc.submit()
    BODY = (g.response.body)
    WD = g.xpath('.//*[@name="WorkingDirectory"]/@value')
    soup = BeautifulSoup(BODY, 'lxml')

    #print(soup)
    print(str(WD))
    wd = WD[19:29]
    #print(wd)
    return WD


def request(it, wd):


    ID = 0
    i = 0
    while i < it:
        try:
            g.setup(post={
                "WorkingDirectory": wd,
                "Exp": "1",
                "CroCommand": "BankSelect:~#Search3;UserFormula:~4_InitFL",
                "surname": "ПОЛЯКОВ",
                "firstname": "ДЕНИС",
                "middlename": "СЕРГЕЕВИЧ",
                "dateofbirth": "19.05.1972",
                "idseries": "1234",
                "idnum": "123456",
                "region": "01",
                "city": "фыва",
                "street": "фыва",
                "house": "1",
                "infoType": "1",
                "exp": "on",
                "rzBRS": "big",
                "go": "Поиск"

            })

            g.go('http://192.168.0.23:81/Scripts/CroISAPI.dll')
            xmlBODY = (g.response.body)
            print('--------------------------------------------------------------' + str(i))


            #soup = BeautifulSoup(xmlBODY, 'lxml')
            #print(soup)


            # g.doc.set_input('surname', 'ПОЛЯКОВ')
            # g.doc.set_input('firstname', 'АЛЕКСЕЙ')
            # g.doc.set_input('middlename', 'НИКОЛАЕВНА')
            # g.doc.set_input('dateofbirth', '19.05.1972')
            # g.doc.set_input('idseries', '1234')
            # g.doc.set_input('idnum', '913410')
            # g.doc.set_input('region', '45')
            # g.doc.set_input('city', 'фыва')
            # g.doc.set_input('street', 'МИЧУРИНА')
            # g.doc.set_input('house', '12')
            # g.doc.set_input('exp', 'on')
            # g.doc.set_input('infoType', '1')
            # g.doc.set_input('rzBRS', 'big')
            # g.doc.set_input('go', 'Поиск')
            # g.doc.set_input('go', 'Поиск')
            # g.doc.submit()
            # xmlBODY = (g.response.body)
            # soup = BeautifulSoup(xmlBODY, 'lxml')
            # print(soup)

            # xmlBODY = str(xmlBODY)
            # result = re.compile("([a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12})")
            # ID = result.findall(xmlBODY)[0]
            # while ID == r'ponse>\n  <CroConnection />\n  <role' or ID =='\'' or len(ID) != 36:
            #     print('ПРОБУЕМ ОТПРАВИТЬСЯ СНОВА')
            #     g.go('https://192.168.0.118/api/request/FL')
            #     xmlBODY = (g.response.body)
            #     xmlBODY = str(xmlBODY)
            #     result = re.compile("([a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12})")
            #     ID = result.findall(xmlBODY)[0]
            # if ID not in ID_list:
            #     ID_list.append(ID)
            #     print(ID + ' sent')


        except Exception as e:
            Exceptions.append(e)
            print(e)

        i += 1





wd = login()

req = 5
THREADS = 5
thread = 0
working_threds =[]

start_time = datetime.now()

try:
    while thread < THREADS:

        t = 't' + str(thread)

        # if thread % sleep_tread == 0:
        #     sleep(sllep_time)

        p = threading.Thread(target=request, name=t, args=[req, wd]) # args - количество запросов
        p.start()
        working_threds.append(p)
        thread += 1

except Exception as e:
    Exceptions.append(e)

for wt in working_threds:       # ждем завершения всех потоков
    wt.join()

end_time = datetime.now()


all_time = end_time - start_time
time_per_sekond = all_time / req

with open(r'C:\log2.txt', 'a') as log:
    log.write(str(start_time) + ' - ' + str(end_time) + ' !!!! total time ' + str(all_time) + ' !!!! ' + '~ seconds_in_request ' + str(time_per_sekond) + '\n')
print('total time ' + str(all_time))
print('~ seconds_in_request ' + str(time_per_sekond))






