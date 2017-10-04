from datetime import datetime

from bs4 import BeautifulSoup
from grab import *
from lxml import html
import threading
from time import sleep

URL = '192.168.0.50:3777'
Exceptions = []


def login(iter):
    g = Grab(timeout=1000, connect_timeout=30)
    i = 0

    try:
        while i < iter:

            g.setup(post= {
                    'Type': 'Login',
                    'Login': 'kdinisv',
                    'Password': '123',
                    },
                    headers= {
                    'Accept-Encoding': 'gzip,deflate',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    }
            )
            go = g.go(URL)
            #print(g.xpath_text(PATH))
            xmlBODY = (go.body)
            lx = html.fromstring(xmlBODY)
            WD = lx.xpath('//text()')[1]
            print('WD ' + str(WD))





            ULFNST = { 'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '1',
                       'FNST' : '1',
                       'OGRN' : '1177746172790',} #0
            ULFNSA = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '1',
                       'FNSA' : '1',
                       'OGRN' : '1177746172790',} #1
            ULGIBDD = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '1',
                       'GIBDD' : '1',
                       'OGRN' : '1177746172790',} #2
            ULBalans = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '1',
                       'Balans' : '1',
                       'OGRN' : '1177746172790',} #3
            ULSVI = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '1',
                       'SVI' : '1',
                       'OGRN' : '1177746172790',} #4
            ULBenef = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '1',
                       'Benef' : '1',
                       'OGRN' : '1177746172790',} #5
            ULAFF = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '1',
                       'AFF' : '1',
                       'OGRN' : '1177746172790',} #6
            ULEmployer = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '1',
                       'Employer' : '1',
                       'OGRN' : '1177746172790',} #7
            ULExtSource = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '1',
                       'ExtSource' : '1',
                       'OGRN' : '1177746172790',} #8

            IPIPT = {'Type': 'Request',
                            'WorkingDirectory' : WD,
                            'Event' : '2',
                            'IPT' : '1',
                            'OGRNIP' : '312751502300034',}  #0
            IPIPA = {'Type': 'Request',
                            'WorkingDirectory' : WD,
                            'Event' : '2',
                            'IPA' : '1',
                            'OGRNIP' : '312751502300034',} #1
            IPExtendedIP = {'Type': 'Request',
                            'WorkingDirectory' : WD,
                            'Event' : '2',
                            'ExtendedIP' : '1',
                            'OGRNIP' : '312751502300034',} #2
            IPEmployer = {'Type': 'Request',
                            'WorkingDirectory' : WD,
                            'Event' : '2',
                            'Employer' : '1',
                            'OGRNIP' : '312751502300034',
                                'FIO' : '',
                                'Region' : '',
                                'City' : '',
                                'Street' :'',
                                'House' : '',
                                'Flat' : '',
                                'Phone' : '',
                          } #3
            IPExtSource = {'Type': 'Request',
                            'WorkingDirectory' : WD,
                            'Event' : '2',
                            'ExtSource' : '1',
                            'OGRNIP' : '312751502300034',} #4

            UL = [ULFNST,
                  ULFNSA,
                  ULGIBDD,
                  ULBalans,
                  ULSVI,
                  ULBenef,
                  ULAFF,
                  ULEmployer,
                  ULExtSource]  # 0
            IP = [IPIPT,
                  IPIPA,
                  IPExtendedIP,
                  IPEmployer,
                  IPExtSource] #1

            Services = [UL,IP]

            g.setup(post=Services[1][3]




            ,
                headers={
                    'Accept-Encoding': 'gzip,deflate',
                    'Content-Type': 'application/x-www-form-urlencoded',
                }
            )
            go = g.go(URL)
            # print(g.xpath_text(PATH))
            xmlBODY = (go.body)
            lx = html.fromstring(xmlBODY)
            RN = lx.xpath('//text()')[1]
            # ANSWER = BeautifulSoup(xmlBODY, 'lxml')
            # print(ANSWER)
            print('RN ' + str(RN))





            sleep(30)

            g.setup(post={
                'Type': 'Answer',
                'WorkingDirectory': WD,
                'RequestNumber' : RN,
                'TypeAnswer' : 'HV'
            },
                headers={
                    'Accept-Encoding': 'gzip,deflate',
                    'Content-Type': 'application/x-www-form-urlencoded',

                }
            )
            go = g.go(URL)
            # print(g.xpath_text(PATH))
            xmlBODY = (go.body)
            lx = html.fromstring(xmlBODY)
            ANS = lx.xpath('//text()')[1]
            ANSWER = BeautifulSoup(xmlBODY, 'lxml')
            print(ANSWER)
            print('ANS ' + str(ANS))




            g.setup(post={
                'Type': 'Logout',
                'WorkingDirectory': WD,
            },
                headers={
                    'Accept-Encoding': 'gzip,deflate',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    #'Content-Length': '47',
                    #'Host': "ips2:777",
                    #'Connection': 'Keep-Alive',
                }
            )
            go = g.go(URL)
            # print(g.xpath_text(PATH))
            xmlBODY = (go.body)
            lx = html.fromstring(xmlBODY)
            ANS = lx.xpath('//text()')[3]
            print('LOGOUT ' + str(ANS))


            i+=1


    except:
     pass








threads = 1    # max 700
thread = 0
working_threds =[]
try:
    while thread < threads:

        t = 't' + str(thread)
        p = threading.Thread(target=login, name=t, args=[1])
        p.start()
        working_threds.append(p)
        thread += 1

except Exception as e:
    Exceptions.append(e)

for wt in working_threds:       # ждем завершения всех потоков
    wt.join()

# for wdg in WORKINGDIRECTORYCLOBAL:
#     print(wdg)

print('kol-vo potokov vsego ' + str(len(working_threds)))
print(Exceptions)