from datetime import datetime, time
import re
from grab import *
from lxml import html
import threading
from time import sleep

ID_list = []

LOCK = threading.RLock()



# # LOCK.acquire()
# #
# # LOCK.release()



Exceptions = []
g = Grab( follow_location= True,reuse_cookies=True, follow_refresh=True, timeout=1000, connect_timeout=30)

def login():
    g.setup(post={'Login':'demo', 'Password': 'demo'})
    g.go('https://192.168.0.118/login')

def request(it):
    start_time = datetime.now()
    ID = 0
    i = 0
    while i < it:
        try:

            g.setup(post={
                "Exp":"1",
                "SurName":"БАЛАЧИЙ",
                "FirstName":"ИРИНА",
                "MiddleName":"АЛЕКСАНДРОВНА",
                "DateOfBirth":"16.09.2016",
                "Seria":"1234",
                "Number":"123456",
                "IssueDate":"",
                "INNExp":"",
                "InfoType":"1",
                "RegionExp":"45",
                "CityExp":"москва",
                "StreetExp":"мос",
                "HouseExp":"3",
                "BuildExp":"",
                "FlatExp":"",
                "RegionExpTmp":"",
                "CityExpTmp":"",
                "StreetExpTmp":"",
                "HouseExpTmp":"",
                "BuildExpTmp":"",
                "FlatExpTmp":"",
                "INNOrgExp":"",
                "OGRNOrgExp":"",
                "INNIPExp":"",
                "OGRNIPExp":"",
                "NameOrgExp":"",
                "FIOIPExp":"",
                "RegionOrgExp":"",
                "RegionIPExp":"",
                "CityOrgExp":"",
                "CityIPExp":"",
                "StreetOrgExp":"",
                "StreetIPExp":"",
                "HouseOrgExp":"",
                "HouseIPExp":"",
                "BuildOrgExp":"",
                "BuildIPExp":"",
                "FlatOrgExp":"",
                "FlatIPExp":"",
                "PhoneExp":"",
                "PhoneOrgExp":"",
                "PhoneIPExp":"",
                "SurNameArch":"",
                "FirstNameArch":"",
                "MiddleNameArch":"",
                "SeriaArch":"",
                "NumberArch":"",

            })



            g.go('https://192.168.0.118/api/request/FL')

            xmlBODY = (g.response.body)
            xmlBODY = str(xmlBODY)
            result = re.compile("([a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12})")
            ID = result.findall(xmlBODY)[0]
            # ID = xmlBODY[114:150]
            # ID = str(ID)[2:38]
            while ID == r'ponse>\n  <CroConnection />\n  <role' or ID =='\'' or len(ID) != 36:
                print('ПРОБУЕМ ОТПРАВИТЬСЯ СНОВА')
                g.go('https://192.168.0.118/api/request/FL')
                xmlBODY = (g.response.body)
                xmlBODY = str(xmlBODY)
                result = re.compile("([a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12})")
                ID = result.findall(xmlBODY)[0]
            if ID not in ID_list:
                ID_list.append(ID)
                print(ID + ' sent')




        except Exception as e:
            Exceptions.append(e)




        # for id in ID_list[::-1]:
        #     URL = 'https://192.168.0.118/download/HTML/' + id

        g.go('https://192.168.0.118/download/HTML/' + str(ID))
        is_answer = g.doc.text_search(u'Вектор заемщика')
        print(str(ID) + ' Answer  ' + str(is_answer))
        while is_answer!=True:
            g.go('https://192.168.0.118/download/HTML/' + str(ID))
            is_answer = g.doc.text_search(u'Вектор заемщика')
            print(str(ID) + ' Answer  ' +str(is_answer))

        i += 1
    end_time = datetime.now()
    all_request_time = end_time - start_time
    request_time = all_request_time/it
    print(str(it) + ' requests finished in time  ' + str(all_request_time))
    print('request time ~ ' + str(request_time))









login()
request(100)

# for _ in range(THREADS_COUNT):
#     #Проход циклом по диапазону чисел количества потоков
#     thread_ = threading.Thread(target=request, args=[10])
#         #Создается поток, target-имя функции, которая являет собой
#         #участок кода, выполняемый многопоточно
#     thread_.start()
#         #Вызывается метод start() , таким образом поток запускается
#     while threading.active_count() >1:
#     #До тех пор, пока количество активных потоков больше 1 (значит,
#     #запущенные потоки продолжают работу)
#        sleep(1)




# threads = 20    # max 700
# thread = 0
# request_threds =[]
# try:
#     while thread < threads:
#
#         t = 't' + str(thread)
#
#         p = threading.Thread(target=request, name=t, args=[2])
#         p.start()
#         request_threds.append(p)
#         thread += 1
#         if thread % 5 == 0:
#             sleep(2)
# except Exception as e:
#     Exceptions.append(e)
#
# for wt in request_threds:       # ждем завершения всех потоков
#     wt.join()

# for wdg in WORKINGDIRECTORYCLOBAL:
#     print(wdg)

# print('kol-vo potokov vsego ' + str(len(request_threds)))
# print(Exceptions)

