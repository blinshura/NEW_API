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
                       'OGRN' : '1177746172790',} # 0
            ULFNSA = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '1',
                       'FNSA' : '1',
                       'OGRN' : '1177746172790',} # 1
            ULGIBDD = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '1',
                       'GIBDD' : '1',
                       'OGRN' : '1177746172790',} # 2
            ULBalans = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '1',
                       'Balans' : '1',
                       'OGRN' : '1177746172790',} # 3
            ULSVI = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '1',
                       'SVI' : '1',
                       'OGRN' : '1177746172790',} # 4
            ULBenef = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '1',
                       'Benef' : '1',
                       'OGRN' : '1177746172790',} # 5
            ULAFF = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '1',
                       'AFF' : '1',
                       'OGRN' : '1177746172790',} # 6
            ULEmployer = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '1',
                       'Employer' : '1',
                       'OGRN' : '1177746172790',} # 7
            ULExtSource = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '1',
                       'ExtSource' : '1',
                       'OGRN' : '1177746172790',} # 8

            IPIPT = {'Type': 'Request',
                            'WorkingDirectory' : WD,
                            'Event' : '2',
                            'IPT' : '1',
                            'OGRNIP' : '312751502300034',}  # 0
            IPIPA = {'Type': 'Request',
                            'WorkingDirectory' : WD,
                            'Event' : '2',
                            'IPA' : '1',
                            'OGRNIP' : '312751502300034',} # 1
            IPExtendedIP = {'Type': 'Request',
                            'WorkingDirectory' : WD,
                            'Event' : '2',
                            'ExtendedIP' : '1',
                            'OGRNIP' : '312751502300034',} # 2
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
                          } # 3
            IPExtSource = {'Type': 'Request',
                            'WorkingDirectory' : WD,
                            'Event' : '2',
                            'ExtSource' : '1',
                            'OGRNIP' : '312751502300034',} # 4

            FLGIBDD = { 'Type': 'Request',
                        'WorkingDirectory' : WD,
                        'Event' : '3',
                        'GIBDD': '1',
                        'SurName' : 'ХРОМОВ',
                        'FirstName' : 'АЛЕКСАНДР',
                        'MiddleName' : 'ВАЛЕРИАНОВИЧ ',
                        'DateOfBirth' :'03.08.1969',
                        'Seria'	: '3213',
                        'Number' : '321321',}  # 0
            FLCASBO = {'Type': 'Request',
                        'WorkingDirectory' : WD,
                        'Event' : '3',
                        'CASBO': '1',
                        'SurName' : 'ХРОМОВ',
                        'FirstName' : 'АЛЕКСАНДР',
                        'MiddleName' : 'ВАЛЕРИАНОВИЧ ',
                        'DateOfBirth' :'03.08.1969',
                        'Seria'	: '3213',
                        'Number' : '321321',}  # 1
            FLCASBR = {'Type': 'Request',
                        'WorkingDirectory' : WD,
                        'Event' : '3',
                        'CASBR': '1',
                        'SurName' : 'ХРОМОВ',
                        'FirstName' : 'АЛЕКСАНДР',
                        'MiddleName' : 'ВАЛЕРИАНОВИЧ ',
                        'DateOfBirth' :'03.08.1969',
                        'Seria'	: '3213',
                        'Number' : '321321',}  # 2
            FLRaiting = {'Type': 'Request',
                        'WorkingDirectory' : WD,
                        'Event' : '3',
                        'Raiting': '1',
                        'SurName' : 'ХРОМОВ',
                        'FirstName' : 'АЛЕКСАНДР',
                        'MiddleName' : 'ВАЛЕРИАНОВИЧ ',
                        'DateOfBirth' :'03.08.1969',
                        'Seria'	: '3213',
                        'Number' : '321321',
                        'IssueDate':'03.08.1969',}  # 3
            FLRaitingR = {'Type': 'Request',
                        'WorkingDirectory' : WD,
                        'Event' : '3',
                        'RaitingR': '1',
                        'SurName' : 'ХРОМОВ',
                        'FirstName' : 'АЛЕКСАНДР',
                        'MiddleName' : 'ВАЛЕРИАНОВИЧ ',
                        'DateOfBirth' :'03.08.1969',
                        'Seria'	: '3213',
                        'Number' : '321321',
                        'IssueDate':'03.08.1969',}  # 4
            FLRaiting_2 = {'Type': 'Request',
                        'WorkingDirectory' : WD,
                        'Event' : '3',
                        'Raiting_2': '1',
                        'SurName' : 'ХРОМОВ',
                        'FirstName' : 'АЛЕКСАНДР',
                        'MiddleName' : 'ВАЛЕРИАНОВИЧ ',
                        'DateOfBirth' :'03.08.1969',
                        'Seria'	: '3213',
                        'Number' : '321321',
                        'IssueDate':'03.08.1969',}  # 5
            FLRaiting_2R = {'Type': 'Request',
                        'WorkingDirectory' : WD,
                        'Event' : '3',
                        'Raiting_2R': '1',
                        'SurName' : 'ХРОМОВ',
                        'FirstName' : 'АЛЕКСАНДР',
                        'MiddleName' : 'ВАЛЕРИАНОВИЧ ',
                        'DateOfBirth' :'03.08.1969',
                        'Seria'	: '3213',
                        'Number' : '321321',
                        'IssueDate':'03.08.1969',}  # 6
            FLFR = {'Type': 'Request',
                        'WorkingDirectory' : WD,
                        'Event' : '3',
                        'FR': '1',
                        'SurName' : 'ХРОМОВ',
                        'FirstName' : 'АЛЕКСАНДР',
                        'MiddleName' : 'ВАЛЕРИАНОВИЧ ',
                        'DateOfBirth' :'03.08.1969',
                        'Seria'	: '3213',
                        'Number' : '321321',}  # 7
            FLAFF = {'Type': 'Request',
                        'WorkingDirectory' : WD,
                        'Event' : '3',
                        'AFF': '1',
                        'SurName' : 'ХРОМОВ',
                        'FirstName' : 'АЛЕКСАНДР',
                        'MiddleName' : 'ВАЛЕРИАНОВИЧ ',
                        'DateOfBirth' :'03.08.1969',
                        'Seria'	: '3213',
                        'Number' : '321321',}  # 8
            FLCKKI = {'Type': 'Request',
                        'WorkingDirectory' : WD,
                        'Event' : '3',
                        'CKKI': '1',
                        'SurName' : 'ХРОМОВ',
                        'FirstName' : 'АЛЕКСАНДР',
                        'MiddleName' : 'ВАЛЕРИАНОВИЧ ',
                        'DateOfBirth' :'03.08.1969',
                        'Seria'	: '3213',
                        'Number' : '321321',
                        'IssueDate':'03.08.1969',}  # 9
            FLSVI = {'Type': 'Request',
                        'WorkingDirectory' : WD,
                        'Event' : '3',
                        'SVI': '1',
                        'SurName' : 'ХРОМОВ',
                        'FirstName' : 'АЛЕКСАНДР',
                        'MiddleName' : 'ВАЛЕРИАНОВИЧ ',
                        'DateOfBirth' :'03.08.1969',
                        'Seria'	: '3213',
                        'Number' : '321321',
                        'InfoType':'1',} # 10
            FLExp = {
                    # Основной блок
                    'Type': 'Request',
                    'WorkingDirectory': WD,
                    'Event': '3',
                    'Exp': '1',
                    'SurName':'ХРОМОВ',
                    'FirstName':'АЛЕКСАНДР',
                    'MiddleName':'ВАЛЕРИАНОВИЧ',
                    'DateOfBirth':'03.08.1969',
                    'Seria':'3213',
                    'Number':'321321',
                    'INNExp':'770404319004',
                    # Блок Адрес Постоянный
                    'RegionExp':'45',
                    'CityExp':'МОСКВА',
                    'StreetExp':'ПОЖАРСКИЙ',
                    'HouseExp':'15',
                    'BuildExp':'',              # или
                    'BuildingExp':'',
                    'FlatExp':'6',
                    'PhoneExp':'',
                    # Блок Адрес Временный
                        # 'RegionExpTmp':'45',
                        # 'CityExpTmp':'МОСКВА',
                        # 'StreetExpTmp':'ПОЖАРСКИЙ',
                        # 'HouseExpTmp':'15',
                        # 'BuildExpTmp':'',
                        # 'BuildingExpTmp':'',
                        # 'FlatExpTmp':'6',
                    # НЕОБЯЗАТЕЛЬНЫЙ блок Поиск архивных данных
                        # 'ExpArch':'',
                        # 'SurNameArch':'',
                        # 'FirstNameArch':'',
                        # 'MiddleNameArch':'',
                        # 'SeriaArch':'',
                        # 'NumberArch':'',
                    # НЕОБЯЗАТЕЛЬНЫЙ блок Проверка работодателя
                    # Роботодатель ЮЛ
                        'OrgExp':'1',
                        'OGRNOrgExp':'1154205015832', # INNOrgExp
                        'NameOrgExp':'ВЕСТА',
                        'RegionOrgExp':'32',
                        'CityOrgExp':'КЕМЕРОВО',
                        'StreetOrgExp':'ЛЕНИНА',          # или
                        'HouseOrgExp':'128',
                        'BuildOrgExp':'',
                        'BuildingOrgExp':'',
                        'FlatOrgExp':'709',
                        'PhoneOrgExp':'',
                        # Роботодатель ИП
                        # 'IPExp':'',
                        # 'OGRNIPExp':'', # INNIPExp
                        # 'FIOIPExp':'',
                        # 'RegionIPExp':'',
                        # 'CityIPExp':'',
                        # 'StreetIPExp':'',
                        # 'HouseIPExp':'',
                        # 'BuildIPExp':'',
                        # 'BuildingIPExp':'',
                        # 'FlatIPExp':'',
                        # 'PhoneIPExp':'',

            }  # 11
            FLExtSource = {
                'Type': 'Request',
                'WorkingDirectory': WD,
                'Event': '3',
                'ExtSource': '1',
                'SurName': 'ХРОМОВ',
                'FirstName': 'АЛЕКСАНДР',
                'MiddleName': 'ВАЛЕРИАНОВИЧ ',
                'DateOfBirth': '03.08.1969',
                'Seria': '3213',
                'Number': '321321',
                'RegionExp': '45'}  # 12

            PASP_UPassporta = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '4',
                       'UPassporta' : '1',
                        'Seria': '4500',
                        'Number': '375473',} # 0
            PASP_PPFMS = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '4',
                       'PPFMS' : '1',
                        'Seria': '4500',
                        'Number': '375473',} # 1

            BSUL_BS = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '5',
                       'BS' : '1',
                        'OGRN': '1177746172790',} # 0
            BSUL_BSPD = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '5',
                       'BSPD' : '1',
                        'OGRN': '1177746172790',} # 1
            BSUL_SVI = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '5',
                       'SVI' : '1',
                        'OGRN': '1177746172790',} # 2

            GIBDD_TS = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '6',
                       'TS' : '1',
                        'GosNumber': 'М982ММ99',
                        #'VIN': '',
                        } # 0
            GIBDD_BCars = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '6',
                       'BCars' : '1',
                        'GosNumber': 'М982ММ99',
                        #'VIN': '',
                           } # 1
            GIBDD_SCars = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '6',
                       'SCars' : '1',
                        'GosNumber': 'М982ММ99',
                        #'VIN': '',
                           } # 2

            BSIP_BIP = {
                'Type': 'Request',
                'WorkingDirectory': WD,
                'Event': '7',
                'BIP': '1',
                'SurName':'ХРОМОВ',
                'FirstName':'АЛЕКСАНДР',
                'MiddleName':'ВАЛЕРИАНОВИЧ',
                'DateOfBirth':'03.08.1969',
                'Seria':'4597',
                'Number':'00522',
                'OGRNIP':'312774618000575',
                'INNExp':'770404319004',
                'RegionExp':'45',
                'CityExp':'МОСКВА',
                'StreetExp':'ПОЖАРСКИЙ',
                'HouseExp':'15',
                'BuildExp':'',
                'BuildingExp':'',
                'FlatExp':'6',
                'PhoneExp':'4956950322',
                # Или Временная регистрация
                #     'RegionExpTmp':'',
                #     'CityExpTmp':'',
                #     'StreetExpTmp':'',
                #     'HouseExpTmp':'',
                #     'BuildExpTmp':'',
                #     'BuildingExpTmp':'',
                #     'FlatExpTmp':'',

            } # 0



            UL = [ULFNST,
                  ULFNSA,
                  ULGIBDD,
                  ULBalans,
                  ULSVI,
                  ULBenef,
                  ULAFF,
                  ULEmployer,
                  ULExtSource
                  ] # 0
            IP = [IPIPT,
                  IPIPA,
                  IPExtendedIP,
                  IPEmployer,
                  IPExtSource
                  ] # 1
            FL = [
                FLGIBDD,
                FLCASBO,
                FLCASBR,
                FLRaiting,
                FLRaitingR,
                FLRaiting_2,
                FLRaiting_2R,
                FLFR,
                FLAFF,
                FLCKKI,
                FLSVI,
                FLExp,
                FLExtSource,
            ] # 2
            PASP = [
                PASP_UPassporta,
                PASP_PPFMS,
            ] # 3
            BSUL = [
                BSUL_BS,
                BSUL_BSPD,
                BSUL_SVI,
            ] # 4
            GIBDD = [
                GIBDD_TS,
                GIBDD_BCars,
                GIBDD_SCars,
            ] # 5
            BSIP = [
                BSIP_BIP,
            ] # 6

            Services = [UL,IP,FL,PASP,BSUL,GIBDD,BSIP]

            g.setup(post=Services[6][0],
                    headers={
                    'Accept-Encoding': 'gzip,deflate',
                    'Content-Type': 'application/x-www-form-urlencoded',
                })
            go = g.go(URL)
            # print(g.xpath_text(PATH))
            xmlBODY = (go.body)
            lx = html.fromstring(xmlBODY)
            RN = lx.xpath('//text()')[1]
            # ANSWER = BeautifulSoup(xmlBODY, 'lxml')
            # print(ANSWER)
            print('RN ' + str(RN))






            ANS = '3'
            while ANS == '3':
                sleep(10)
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
                ANS = str(ANS)
                ANSWER = BeautifulSoup(xmlBODY, 'lxml')
                if ANS != '3' : print(ANSWER)
                print('ANS ' + ANS)




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