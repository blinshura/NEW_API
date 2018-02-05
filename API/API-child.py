from datetime import datetime

import re
from bs4 import BeautifulSoup
from grab import *
from lxml import html
import threading
from time import sleep


import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# import logging
# logger = logging.getLogger('grab')
# logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.DEBUG)



URL = '192.168.0.135:3777'
Exceptions = []
ERRORS = []


def login(iter):
    g = Grab(timeout=1000, connect_timeout=30, debug_post=False, reuse_cookies=False)
    i = 0

    try:
        while i < iter:

            g.setup(post= {
                    'Type': 'Login',
                    'Login': 'demo',
                    'Password': 'demo',
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
                       'FNST': '1',
                       'OGRN' : '1177746172790',
                       #'INN': '3213213211',
                       'zapros': 'UL-FNST'} # 0
            ULFNSA = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '1',
                       'FNSA' : '1',
                       'OGRN' : '1177746172790',
                      'zapros': 'UL-FNSA'} # 1
            ULGIBDD = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '1',
                       'GIBDD' : '1',
                       'OGRN' : '1177746172790',
                       'zapros': 'UL-GIBDD'} # 2
            ULBalans = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '1',
                       'Balans' : '1',
                       'OGRN' : '1177746172790',
                        'zapros': 'UL-Balans'} # 3
            ULSVI = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '1',
                       'SVI' : '1',
                       'OGRN' : '1177746172790',
                     'zapros': 'UL-SVI'} # 4
            ULBenef = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '1',
                       'Benef' : '1',
                       'OGRN' : '1177746172790',
                       'zapros': 'UL-Benef'} # 5
            ULAFF = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '1',
                       'AFF' : '1',
                       'OGRN' : '1177746172790',
                     'zapros': 'UL-AFF'} # 6
            ULEmployer = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '1',
                       'Employer' : '1',
                       'OGRN' : '1177746172790',
                          'zapros': 'UL-Employer'} # 7
            ULExtSource = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '1',
                       'ExtSource' : '1',
                       'OGRN' : '1177746172790',
                           'zapros': 'UL-ExtSource'} # 8

            IPIPT = {'Type': 'Request',
                            'WorkingDirectory' : WD,
                            'Event' : '2',
                            'IPT' : '1',
                            #'OGRNIP' : '312751502300034',
                     'INNIP': '231400212630',
                     'zapros': 'IP-IPT'}  # 0
            IPIPA = {'Type': 'Request',
                            'WorkingDirectory' : WD,
                            'Event' : '2',
                            'IPA' : '1',
                            'OGRNIP' : '312751502300034',
                     'zapros': 'IP-IPA'} # 1
            IPExtendedIP = {'Type': 'Request',
                            'WorkingDirectory' : WD,
                            'Event' : '2',
                            'ExtendedIP' : '1',
                            'OGRNIP' : '312751502300034',
                            'zapros': 'IP-ExtendedIP'} # 2
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
                          'zapros': 'IP-Employer'
                          } # 3
            IPExtSource = {'Type': 'Request',
                            'WorkingDirectory' : WD,
                            'Event' : '2',
                            'ExtSource' : '1',
                            'OGRNIP' : '312751502300034',
                           'zapros': 'IP-ExtSource'} # 4

            FLGIBDD = { 'Type': 'Request',
                        'WorkingDirectory' : WD,
                        'Event' : '3',
                        'GIBDD': '1',
                        'SurName' : 'ХРОМОВ',
                        'FirstName' : 'АЛЕКСАНДР',
                        'MiddleName' : 'ВАЛЕРИАНОВИЧ',
                        'DateOfBirth' :'31.09.1988',
                        'Seria'	: '3213',
                        'Number' : '321321',
                        'zapros': 'FL-GIBDD'}  # 0
            FLCASBO = {'Type': 'Request',
                        'WorkingDirectory' : WD,
                        'Event' : '3',
                        'CASBO': '1',
                        'SurName' : 'ХРОМОВ',
                        'FirstName' : 'АЛЕКСАНДР',
                        'MiddleName' : 'ВАЛЕРИАНОВИЧ',
                        'DateOfBirth' :'03.08.1969',
                        'Seria'	: '3213',
                        'Number' : '321321',
                       'zapros': 'FL-CASBO'}  # 1
            FLCASBR = {'Type': 'Request',
                        'WorkingDirectory' : WD,
                        'Event' : '3',
                        'CASBR': '1',
                        'SurName' : 'ХРОМОВ',
                        'FirstName' : 'АЛЕКСАНДР',
                        'MiddleName' : 'ВАЛЕРИАНОВИЧ',
                        'DateOfBirth' :'03.08.1969',
                        'Seria'	: '3213',
                        'Number' : '321321',
                       'zapros': 'FL-CASBR'}  # 2
            FLRaiting = {'Type': 'Request',
                        'WorkingDirectory' : WD,
                        'Event' : '3',
                        'Raiting': '1',
                        'SurName' : 'ХРОМОВ',
                        'FirstName' : 'АЛЕКСАНДР',
                        'MiddleName' : 'ВАЛЕРИАНОВИЧ',
                        'DateOfBirth' :'03.08.1969',
                        'Seria'	: '3213',
                        'Number' : '321321',
                        'IssueDate':'03.08.1969',
                         'zapros': 'FL-Raiting'}  # 3
            FLRaitingR = {'Type': 'Request',
                        'WorkingDirectory' : WD,
                        'Event' : '3',
                        'RaitingR': '1',
                          'SurName': 'ХРОМОВ',
                          'FirstName': 'АЛЕКСАНДР',
                          'MiddleName': 'ВАЛЕРИАНОВИЧ',
                        'DateOfBirth' :'03.08.1969',
                        'Seria'	: '3213',
                        'Number' : '321321',
                        'IssueDate':'03.08.1969',
                          'zapros': 'FL-RaitingR'}  # 4
            FLRaiting_2 = {'Type': 'Request',
                        'WorkingDirectory' : WD,
                        'Event' : '3',
                        'Raiting_2': '1',
                        'SurName' : 'ХРОМОВ',
                        'FirstName' : 'АЛЕКСАНДР',
                        'MiddleName' : 'ВАЛЕРИАНОВИЧ',
                        'DateOfBirth' :'03.08.1969',
                        'Seria'	: '3213',
                        'Number' : '321321',
                        'IssueDate':'03.08.1969',
                           'zapros': 'FL-Raiting_2'}  # 5
            FLRaiting_2R = {'Type': 'Request',
                        'WorkingDirectory' : WD,
                        'Event' : '3',
                        'Raiting_2R': '1',
                        'SurName' : 'ХРОМОВ',
                        'FirstName' : 'АЛЕКСАНДР',
                        'MiddleName' : 'ВАЛЕРИАНОВИЧ',
                        'DateOfBirth' :'03.08.1969',
                        'Seria'	: '3213',
                        'Number' : '321321',
                        'IssueDate':'03.08.1969',
                            'zapros': 'FL-Raitin_2R'}  # 6
            FLFR = {'Type': 'Request',
                        'WorkingDirectory' : WD,
                        'Event': '3',
                        'FR': '1',
                        'SurName' : 'ХРОМОВ',
                        'FirstName' : 'АЛЕКСАНДР',
                        'MiddleName' : 'ВАЛЕРИАНОВИЧ',
                        'DateOfBirth': '03.08.1969',
                        'Seria': '3213',
                        'Number': '321321',
                    'zapros': 'FL-FR'}  # 7
            FLAFF = {'Type': 'Request',
                        'WorkingDirectory' : WD,
                        'Event' : '3',
                        'AFF': '1',
                        'SurName' : 'ХРОМОВ',
                        'FirstName' : 'АЛЕКСАНДР',
                        'MiddleName' : 'ВАЛЕРИАНОВИЧ',
                        'DateOfBirth' :'31.09.1988',
                        'Seria'	: '3213',
                        'Number' : '321321',
                     'zapros': 'FL-AFF'}  # 8
            FLCKKI = {'Type': 'Request',
                        'WorkingDirectory' : WD,
                        'Event' : '3',
                        'CKKI': '1',
                        'SurName' : 'ХРОМОВ',
                        'FirstName' : 'АЛЕКСАНДР',
                        'MiddleName' : 'ВАЛЕРИАНОВИЧ',
                        'DateOfBirth' :'03.08.1969',
                        'Seria'	: '3213',
                        'Number' : '321321',
                        'IssueDate':'03.08.1969',
                      'zapros': 'FL-CKKI'}  # 9
            FLSVI = {'Type': 'Request',
                        'WorkingDirectory' : WD,
                        'Event' : '3',
                        'SVI': '1',
                        'SurName' : 'ХРОМОВ',
                        'FirstName' : 'АЛЕКСАНДР',
                        'MiddleName' : 'ВАЛЕРИАНОВИЧ',
                        'DateOfBirth' :'03.08.1969',
                        'Seria'	: '3213',
                        'Number' : '321321',
                        'InfoType':'1',
                     'zapros': 'FL-SVI'} # 10
            FLExp = {
                    # Основной блок
                    'Type': 'Request',
                    'WorkingDirectory': WD,
                    'Event': '3',
                    'Exp': '1',
                    'SurName' : 'ХРОМОВ',
                    'FirstName' : 'АЛЕКСАНДР',
                    'MiddleName' : 'ВАЛЕРИАНОВИЧ',
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

                'zapros': 'FL-Exp'
            }  # 11
            FLExtSource = {
                'Type': 'Request',
                'WorkingDirectory': WD,
                'Event': '3',
                'ExtSource': '1',
                'SurName' : 'ХРОМОВ',
                'FirstName' : 'АЛЕКСАНДР',
                'MiddleName' : 'ВАЛЕРИАНОВИЧ',
                'DateOfBirth': '03.08.1969',
                'Seria': '3213',
                'Number': '321321',
                'RegionExp': '45',
                             'zapros': 'FL-ExtSource'}  # 12

            PASP_UPassporta = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '4',
                       'UPassporta' : '1',
                        'Seria': '4500',
                        'Number': '375473',
                               'zapros': 'Pasp-UPassporta'} # 0
            PASP_PPFMS = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '4',
                       'PPFMS' : '1',
                        'Seria': '4500',
                        'Number': '375473',
                          'zapros': 'Pasp-PPFMS'} # 1

            BSUL_BS = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '5',
                       'BSUL' : '1',
                        'OGRN': '1177746172790',
                       'zapros': 'BSUL-BS'} # 0
            BSUL_BSPD = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '5',
                       'BSPD' : '1',
                        'OGRN': '1177746172790',
                         'zapros': 'BSUL-BSPD'} # 1
            BSUL_SVI = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '5',
                       'SVI' : '1',
                        'OGRN': '1177746172790',
                        'zapros': 'BSUL-SVI'} # 2

            GIBDD_TS = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '6',
                       'TS' : '1',
                        'GosNumber': 'M775XY27',
                        #'VIN': '',
                        'zapros': 'GIBDD-TS'
                        } # 0
            GIBDD_BCars = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '6',
                       'BCars' : '1',
                        'GosNumber': 'M775XY27',
                        #'VIN': '',
                           'zapros': 'GIBDD-BCars'
                           } # 1
            GIBDD_SCars = {'Type': 'Request',
                       'WorkingDirectory' : WD,
                       'Event' : '6',
                       'SCars' : '1',
                        'GosNumber': 'M775XY27',
                        #'VIN': '',
                           'zapros': 'GIBDD-SCars'
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
                'zapros': 'PSIP-BIP'
            } # 0

            IDFL = {
                'Type': 'Request',
                'WorkingDirectory': WD,
                'Event': '8',
                'IDFL': '1',

                'SurName': 'ХРОМОВ',
                'FirstName': 'АЛЕКСАНДР',
                'MiddleName': 'ВАЛЕРИАНОВИЧ',
                'DateOfBirth': '03.08.1969',
                'Seria': '4597',
                'Number': '00522',
                'Address': '',
                'Phone': '',
                'GosNumber': '',
                'INNIP': '',
                'OGRN': '',
                'OGRNIP': '',

                #        ФИО И Дата рождения
                # ИЛИ    ФИО И Адрес
                # ИЛИ    ФИО И Номер телефона
                # ИЛИ    ФИО И ОГРН организации
                # ИЛИ    ФИО И Паспорт(серия и номер)
                # ИЛИ    ФИО И ИНН
                # ИЛИ    ФИО И Номер трансп.средства
                # ИЛИ    ФИО И ОГРНИП
                # ИЛИ    Паспорт(серия и номер)
                # ИЛИ    ИНН
                # ИЛИ    Номер трансп.средства
                # ИЛИ    ОГРНИП
                'zapros': 'IDFL'
            } # 0

            BSUL_RASH = {
                'Type': 'Request',
                'Event': '9',
                'BSR' : '1',
                'WorkingDirectory': WD,
                # -----------------------------------------------------------------------------------------------------------------------
                'NameOrg': 'ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ "НЕОКОМПАНИ"',
                'OGRN': '1066367043038',
                'INN': '6367053858',
                'KPP': '636701001',
                'RegistrationDate': '25.03.1994',
                'authCapital': '10000',
                'OKVED': '14.12',
                # -----------------------------------------------------------------------------------------------------------------------
                'addressList[0][addressType]': 'L',
                'addressList[0][Region]': '80',
                'addressList[0][City]': 'УФА',
                'addressList[0][Street]': 'МЕНДЕЛЕЕВА',
                'addressList[0][House]': '134',
                'addressList[0][Build]': '10',  ###
                'addressList[0][Building]': '',  ###
                'addressList[0][Office]': '',  ###

                'contactInfo[0][Phone]': '4958555668',
                'contactInfo[0][Fax]': '4959555668',  ###
                # Директор
                'leaderInfoList[0][LeaderCode]': 'L1',
                'leaderInfoList[0][SurName]': 'Ахметов',
                'leaderInfoList[0][FirstName]': 'Фаиль',
                'leaderInfoList[0][MiddleName]': 'Сагитович',  ###
                'leaderInfoList[0][DateOfBirth]': '22.01.1963',
                'leaderInfoList[0][Seria]': '8097',
                'leaderInfoList[0][Number]': '011436',
                # ФЛ Участники
                'participantInfoList[0][ParticipantCode]': 'P1',
                'participantInfoList[0][SurName]': 'Карпов',
                'participantInfoList[0][FirstName]': 'Сергей',
                'participantInfoList[0][MiddleName]': 'Владимирович',  ###
                'participantInfoList[0][DateOfBirth]': '24.06.1974',
                'participantInfoList[0][Seria]': '8004',
                'participantInfoList[0][Number]': '181211',
                'participantInfoList[0][AuthCapShare]': '54000',
                # ЮЛ Участники
                'legalInfoList[0][OGRN]': '1087746801130',
                'legalInfoList[0][AuthCapShare]': '16000',
                # -----------------------------------------------------------------------------------------------------------------------
                'addressList[1][addressType]': 'F',
                'addressList[1][Region]': '',
                'addressList[1][City]': 'Москва',
                'addressList[1][Street]': 'СЕМЕНОВСКАЯ Б',
                'addressList[1][House]': '40',
                'addressList[1][Build]': '',
                'addressList[1][Building]': '18',
                'addressList[1][Office]': '',

                'contactInfo[1][Phone]': '4990007878',
                'contactInfo[1][Fax]': '4990007870',

                'leaderInfoList[1][LeaderCode]': 'L2',
                'leaderInfoList[1][SurName]': 'ЛИЧАГИН',
                'leaderInfoList[1][FirstName]': 'ПАВЕЛ',
                'leaderInfoList[1][MiddleName]': 'АНАТОЛЬЕВИЧ',
                'leaderInfoList[1][DateOfBirth]': '10.10.1965',
                'leaderInfoList[1][Seria]': '4321',
                'leaderInfoList[1][Number]': '654321',

                'participantInfoList[1][ParticipantCode]': 'P1',
                'participantInfoList[1][SurName]': 'ЛИЧАГИН',
                'participantInfoList[1][FirstName]': 'ПАВЕЛ',
                'participantInfoList[1][MiddleName]': '',
                'participantInfoList[1][DateOfBirth]': '10.10.1970',
                'participantInfoList[1][Seria]': '1234',
                'participantInfoList[1][Number]': '123456',
                'participantInfoList[1][AuthCapShare]': '1000',

                'legalInfoList[1][OGRN]': '1027700107599',
                'legalInfoList[1][AuthCapShare]': '15000',
                'zapros': 'BSUL-Rash'
            } # 0



            UL = [ULFNST,
                  ULFNSA,
                  #ULGIBDD,
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
                #FLGIBDD,
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
            ID_FL = [
                IDFL
            ] # 7
            BS_R = [
                BSUL_RASH
            ] # 8

            Services = [UL,
                        IP,
                        FL,
                        PASP,
                        BSUL,
                        #GIBDD,
                        BSIP,
                        ID_FL,
                        BS_R]

            # ----------------------Основной цикл--------------------------
            for i in Services:
                for m in i:
            # ------------------------------------------------

            # -----------------------Ручной цикл----------------------------
            #services = FL
            #for m in services:
            # ---------------------------------------------------

            # ----------------------------Точечнй запрос-------------------------------
            # for i in range(1):
            #     for ii in range(1):
            #         m = FLCKKI
            # -----------------------------------------------------------
                    sleep(1)
                    g.setup(post=m,
                            headers={
                            'Accept-Encoding': 'gzip,defl,utf-8',
                            'Content-Type': 'application/x-www-form-urlencoded',
                        })
                    go = g.go(URL)
                    # print(g.xpath_text(PATH))
                    xmlBODY = (go.body)
                    lx = html.fromstring(xmlBODY)
                    RN = lx.xpath('//text()')[1]
                    re1 = "[A-Z0-9]{8}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{12}"
                    rg = re.compile(re1,re.IGNORECASE|re.DOTALL)
                    r = rg.search(RN)
                    if  r:
                        # ANSWER = BeautifulSoup(xmlBODY, 'lxml')
                        # print(ANSWER)
                        print('RN ' + str(RN))

                        print(m['zapros'])
                    else:
                        print(RN)
                        print(m['zapros'])
                        ERRORS.append(m['zapros'])
                        ERRORS.append(RN)
                        ERRORS.append('---------------------------')






                    ANS = '3'
                    tryes = 30
                    while ANS == '3' and tryes >= 1:
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

                        # Очистка ответа
                        if ANS != '3' :
                            ANSWER = str(ANSWER)
                            clean_answer = ANSWER[54267:]

                            clean_answer = clean_answer.replace('</tr>', '')
                            clean_answer = clean_answer.replace('</td>', '')
                            clean_answer = clean_answer.replace('<tr>', '')
                            clean_answer = clean_answer.replace('<td>', '')
                            clean_answer = clean_answer.replace('</thead>', '')
                            clean_answer = clean_answer.replace('<thead>', '')
                            clean_answer = clean_answer.replace('</tbody>', '')
                            clean_answer = clean_answer.replace('<tbody>', '')
                            clean_answer = clean_answer.replace('</th>', '')
                            clean_answer = clean_answer.replace('<th>', '')
                            clean_answer = clean_answer.replace('</table>', '')
                            clean_answer = clean_answer.replace('</div>', '')
                            clean_answer = clean_answer.replace('<h3 class="text-center">', '')
                            clean_answer = clean_answer.replace('</h3>', '')
                            clean_answer = clean_answer.replace('</div>', '')
                            clean_answer = clean_answer.replace('<table class=', '')
                            clean_answer = clean_answer.replace('<li>', '')
                            clean_answer = clean_answer.replace('</answerhtml></documents></answer></body></html><html><p>', '')
                            clean_answer = clean_answer.replace(']]&gt;</p></html>', '')
                            clean_answer = clean_answer.replace('<p><strong>', '')
                            clean_answer = clean_answer.replace('<ol class="condenced">', '')
                            clean_answer = clean_answer.replace('<h2>', '')
                            clean_answer = clean_answer.replace('</h2>', '')
                            clean_answer = clean_answer.replace('<div class="js_section">', '')
                            clean_answer = clean_answer.replace('</strong>', '')
                            clean_answer = clean_answer.replace('</p>', '')
                            clean_answer = clean_answer.replace('</ul>', '')
                            clean_answer = clean_answer.replace('</span></p>', '')
                            clean_answer = clean_answer.replace('<span>', '')
                            clean_answer = clean_answer.replace('</li>', '')
                            clean_answer = clean_answer.replace('</ol>', '')
                            clean_answer = clean_answer.replace('<p class="note text-muted"><i>', '')
                            clean_answer = clean_answer.replace('<h3 class="text-center" data-count', '')
                            clean_answer = clean_answer.replace('"table fns">', '')
                            clean_answer = clean_answer.replace('<h2 class="text-center">', '')
                            clean_answer = clean_answer.replace('="0"', '')
                            clean_answer = clean_answer.replace('\n\n', '\n')
                            clean_answer = clean_answer.replace('\n\n', '\n')
                            clean_answer = clean_answer.replace('<div>', '')
                            clean_answer = clean_answer.replace('<h3>', '')
                            clean_answer = clean_answer.replace('</span>', '')
                            clean_answer = clean_answer.replace('</i>', '')
                            clean_answer = clean_answer.replace('title=', '')
                            clean_answer = clean_answer.replace('<p>', '')
                            clean_answer = clean_answer.replace('<h5>', '')
                            clean_answer = clean_answer.replace('</h5>', '')
                            clean_answer = clean_answer.replace('<div class="js_section intro"', '')
                            clean_answer = clean_answer.replace('<h3>', '')
                            clean_answer = clean_answer.replace('<td class="legend"', '')
                            clean_answer = clean_answer.replace('<td class="linked text-center"', '')
                            clean_answer = clean_answer.replace('<td class="numered text-center"', '')
                            clean_answer = clean_answer.replace('<td class="legend"', '')

                            clean_answer = clean_answer.replace('>', '')



                            print(clean_answer)


                        print('ANS ' + ANS)
                        tryes -= 1
                        if ANS == '3' and tryes < 1:
                            ERRORS.append(m['zapros'])
                            ERRORS.append(RN + ' Не дождались ответа')
                            ERRORS.append('---------------------------')
                            print(' Не дождались ответа')
                    print('-----------------------------------------------------------------------------------------')



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
print('ERRORS:')
for i in ERRORS:
    print(i)