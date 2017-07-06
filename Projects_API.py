from datetime import datetime
from grab import *
from lxml import html
import threading
from time import sleep


URL = '192.168.0.49:777'
PATH = '*'
WORKINGDIRECTORYCLOBAL = []
time = []
oshibkaGlobal = []
zaprosGlobal = []
Exceptions = []

def login(iter):
    i = 0
    startTime1 = datetime.now()
    workingDirectory = []
    time = []
    oshibka = 0
    zapros = 0

    try:
        while i < iter:
            startTime = datetime.now()
            g = Grab(timeout=1000, connect_timeout=30)
            g.setup(post= {
                    'Type': 'Login',
                    'Login': 'Test_61959959',
                    'Password': '5253325'
                    },
                    headers= {
                    'Accept-Encoding': 'gzip,deflate',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Content-Length': '47',
                    'Host': "ips2:777",
                    'Connection': 'Keep-Alive',
                    }

            )

            go = g.go(URL)
            #print(g.xpath_text(PATH))
            xmlBODY = (go.body)
            lx = html.fromstring(xmlBODY)


            WD = lx.xpath('//text()')[1]
            workingDirectory.append(WD)

            endTime = datetime.now()
            requestTime = endTime - startTime

            print('request time: ', requestTime)
            #print (xmlBODY.decode('utf-8'))
            print(WD)

            i += 1
            print('nomer zaprosa v potoke ' + str(i))
            print('\n')
            zapros += 1

            g = Grab(timeout=1000, connect_timeout=30)
            g.setup(post={
                'Type': 'Logout',
                'WorkingDirectory': WD,
            },
                headers={
                    'Accept-Encoding': 'gzip,deflate',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Content-Length': '47',
                    'Host': "ips2:777",
                    'Connection': 'Keep-Alive',
                }

            )

        endTime1 = datetime.now()
        totalTime1 = endTime1 - startTime1
        time.append([startTime1, endTime1])

        #print('start: ', startTime1, 'end: ', endTime1, 'total: ', totalTime1)
        #print(workingDirectory)

        t = time[len(time)-1][1] - time[0][0]
        time.append(t)
        print('---------------------------------------------------------------')
        print('TOTAL time: ', t)
        print('\n')

        WORKINGDIRECTORYCLOBAL.append(workingDirectory)


    except:
        oshibka += 1

    zaprosGlobal.append(zapros)
    oshibkaGlobal.append(oshibka)
    z = 0
    for i in zaprosGlobal:
        z += i
    print('zaprosov', z)

    o = 0
    for i in oshibkaGlobal:
        o +=i
    print('oshibok', o)



def request():
    pass






threads = 10    # max 700
thread = 0
working_threds =[]
try:
    while thread < threads:

        t = 't' + str(thread)

        p = threading.Thread(target=login, name=t, args=[10])
        p.start()
        working_threds.append(p)
        thread += 1
        if thread % 50 == 0:
            sleep(2)
except Exception as e:
    Exceptions.append(e)

for wt in working_threds:       # ждем завершения всех потоков
    wt.join()

# for wdg in WORKINGDIRECTORYCLOBAL:
#     print(wdg)

print('kol-vo potokov vsego ' + str(len(working_threds)))
print(Exceptions)

