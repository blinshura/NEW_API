import json

import re
from time import sleep

import requests
from lxml import html

URL = 'http://127.0.0.1:3341/'#'http://127.0.0.1:3336/' #http://vips1/ #https://ips3:888/ #http://127.0.0.1:3333/
loginURL = URL + 'login'
billingURL = URL + 'api/billing/'
requestURL = URL + 'api/request/'
pushURL = URL +  'admin/api/user/info'

billingFLURL = billingURL + 'FL'
billingULURL = billingURL + 'UL'
billingIPURL = billingURL + 'IP'
billingADURL = billingURL + 'AD'
billingPASPURL = billingURL + 'UP'
billingGIBDDURL = billingURL + 'TS'

requestFLURL = requestURL + 'FL'
requestULURL = requestURL + 'UL'
requestIPURL = requestURL + 'IP'
requestADURL = requestURL + 'AD'
requestPASPURL = requestURL + 'UP'
requestGIBDDURL = billingURL + 'TS'


LOGIN = 'demo'#'demo' #'Svetka' #'ander_автомат'
PASSWORD = 'demo'#'Gfd!1qaz40' #'153759' #'687dd78R'


WD = ''
RN = ''
subsystemBilling = {}
ERRORS = []
RNs = {}
S = requests.Session()




IDFL = {
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '8',
    'IDFL': '1',

     #'SurName': 'ПОНАМАРЕВА',
     #'FirstName': 'ИРИНА',
     #'MiddleName': 'ЮРЬЕВНА',
    #'DateOfBirth': '11.01.1966',
     'Seria': '4004',
     'Number': '946593',
    # 'Address': '40 САНКТ ПЕТЕРБУРГ ВОЗНЕСЕНСКИЙ 34 1',
    #'Phone': '1111111111',
    #'GosNumber': '',
    #'INNIP': '',
    #'OGRN': '1056900010375',
    #'OGRNIP': '',
    # "RegionExp": '40',
    # "CityExp": 'САНКТ ПЕТЕРБУРГ',
    # "StreetExp": 'ВОЗНЕСЕНСКИЙ',
    # "HouseExp": '34',
    # "BuildExp": '1',
    # "FlatExp": '',





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
    'zapros': 'IDFL',
    'url': billingFLURL
} # 0
FLGIBDD = {'Type': 'Request',
           'WorkingDirectory': WD,
           'Event': '3',
           'GIBDD': '1',
           'SurName': 'ХРОМОВ',
           'FirstName': 'АЛЕКСАНДР',
           'MiddleName': 'ВАЛЕРИАНОВИЧ',
           'DateOfBirth': '31.09.1988',
           'Seria': '3213',
           'Number': '321321',
           'zapros': 'GIBDD',
    'url': billingFLURL}  # 0
CASBO = {'Type': 'Request',
           'WorkingDirectory': WD,
           'Event': '3',
           'CASBO': '1',
           'SurName': 'ХРОМОВ',
           'FirstName': 'АЛЕКСАНДР',
           'MiddleName': 'ВАЛЕРИАНОВИЧ',
           'DateOfBirth': '03.08.1969',
           'Seria': '4597',
           'Number': '005229',
           'zapros': 'CASBO',
    'url': billingFLURL} # 1
CASBR = {'Type': 'Request',
           'WorkingDirectory': WD,
           'Event': '3',
           'CASBR': '1',
           'SurName': 'ХРОМОВ',
           'FirstName': 'АЛЕКСАНДР',
           'MiddleName': 'ВАЛЕРИАНОВИЧ',
           'DateOfBirth': '03.08.1969',
           'Seria': '4597',
           'Number': '005229',
           'zapros': 'CASBR',
    'url': billingFLURL} # 2
Raiting = {'Type': 'Request',
             'WorkingDirectory': WD,
             'Event': '3',
             'Raiting': '1',
             'SurName': 'ХРОМОВ',
             'FirstName': 'АЛЕКСАНДР',
             'MiddleName': 'ВАЛЕРИАНОВИЧ',
             'DateOfBirth': '03.08.1969',
             'Seria': '4597',
             'Number': '005229',
             'IssueDate': '03.08.1969',
             'zapros': 'Raiting',
    'url': billingFLURL} # 3
RaitingR = {'Type': 'Request',
              'WorkingDirectory': WD,
              'Event': '3',
              'RaitingR': '1',
              'SurName': 'ХРОМОВ',
              'FirstName': 'АЛЕКСАНДР',
              'MiddleName': 'ВАЛЕРИАНОВИЧ',
              'DateOfBirth': '03.08.1969',
              'Seria': '4597',
              'Number': '005229',
              'IssueDate': '03.08.1969',
              'zapros': 'RaitingR',
    'url': billingFLURL} # 4
Raiting_2 = {'Type': 'Request',
               'WorkingDirectory': WD,
               'Event': '3',
               'Raiting_2': '1',
               'SurName': 'ХРОМОВ',
               'FirstName': 'АЛЕКСАНДР',
               'MiddleName': 'ВАЛЕРИАНОВИЧ',
               'DateOfBirth': '03.08.1969',
               'Seria': '4597',
               'Number': '005229',
               'IssueDate': '03.08.1969',
               'zapros': 'Raiting_2',
    'url': billingFLURL}  # 5
Raiting_2R = {'Type': 'Request',
                'WorkingDirectory': WD,
                'Event': '3',
                'Raiting_2R': '1',
                'SurName': 'ХРОМОВ',
                'FirstName': 'АЛЕКСАНДР',
                'MiddleName': 'ВАЛЕРИАНОВИЧ',
                'DateOfBirth': '03.08.1969',
                'Seria': '4597',
                'Number': '005229',
                'IssueDate': '03.08.1969',
                'zapros': 'Raiting_2R',
              'url': billingFLURL} # 6
Raiting_3R = {'Type': 'Request',
                'WorkingDirectory': WD,
                'Event': '3',
                'Raiting_3R': '1',
                'SurName': 'ХРОМОВ',
                'FirstName': 'АЛЕКСАНДР',
                'MiddleName': 'ВАЛЕРИАНОВИЧ',
                'DateOfBirth': '03.08.1969',
                'Seria': '4597',
                'Number': '005229',
                'IssueDate': '03.08.1969',
                'zapros': 'Raiting_3R',
                'url': billingFLURL}
Raiting_4R = {'Type': 'Request',
                'WorkingDirectory': WD,
                'Event': '3',
                'Raiting_4R': '1',
                'SurName': 'ХРОМОВ',
                'FirstName': 'АЛЕКСАНДР',
                'MiddleName': 'ВАЛЕРИАНОВИЧ',
                'DateOfBirth': '03.08.1969',
                'Seria': '4597',
                'Number': '005229',
                'IssueDate': '03.08.1969',
                'RegionExp': '45',
                'CityExp':	'москва',
                'StreetExp': 'ленина',
                'HouseExp':	'1',
                'zapros': 'Raiting_4R',
                'url': billingFLURL}
# FLFR = {'Type': 'Request',
#             'WorkingDirectory' : WD,
#             'Event': '3',
#             'FR': '1',
#             'SurName' : 'ХРОМОВ',
#             'FirstName' : 'АЛЕКСАНДР',
#             'MiddleName' : 'ВАЛЕРИАНОВИЧ',
#             'DateOfBirth': '03.08.1969',
#             'Seria': '3213',
#             'Number': '321321',
#         'zapros': 'FR',
#     'url': billingFLURL}  # 7
AFF = {'Type': 'Request',
         'WorkingDirectory': WD,
         'Event': '3',
         'AFF': '1',
         'SurName': 'ХРОМОВ',
         'FirstName': 'АЛЕКСАНДР',
         'MiddleName': 'ВАЛЕРИАНОВИЧ',
         'DateOfBirth': '03.08.1969',
         'Seria': '4597',
         'Number': '005229',
         'zapros': 'AFF',
    'url': billingFLURL}  # 8
CKKI = {'Type': 'Request',
          'WorkingDirectory': WD,
          'Event': '3',
          'CKKI': '1',
          'SurName': 'ХРОМОВ',
          'FirstName': 'АЛЕКСАНДР',
          'MiddleName': 'ВАЛЕРИАНОВИЧ',
          'DateOfBirth': '03.08.1969',
          'Seria': '4597',
          'Number': '005229',
          'IssueDate': '03.08.1969',
          'zapros': 'CKKI',
    'url': billingFLURL}  # 9
SVI = {'Type': 'Request',
         'WorkingDirectory': WD,
         'Event': '3',
         'SVI': '1',
         'SurName': 'ХРОМОВ',
         'FirstName': 'АЛЕКСАНДР',
         'MiddleName': 'ВАЛЕРИАНОВИЧ',
         'DateOfBirth': '03.08.1969',
         'Seria': '4597',
         'Number': '005229',
         'InfoType': '1',
         'zapros': 'SVI',
    'url': billingFLURL}  # 10
Exp = {
    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': u'Владимирович',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    #'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '+79263830685',
    # Блок Адрес Временный
    # 'RegionExpTmp':'45',
    # 'CityExpTmp':('МОСКВА').encode('utf8'),
    # 'StreetExpTmp':('ПОЖАРСКИЙ').encode('utf8'),
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
    # 'OrgExp': '1',
    # 'OGRNOrgExp': '1154205015832',  # INNOrgExp
    # 'NameOrgExp': 'ВЕСТА',
    # 'RegionOrgExp': '32',
    # 'CityOrgExp': 'КЕМЕРОВО',
    # 'StreetOrgExp': 'ЛЕНИНА',  # или
    # 'HouseOrgExp': '128',
    # 'BuildOrgExp': '',
    # 'BuildingOrgExp': '',
    # 'FlatOrgExp': '709',
    # 'PhoneOrgExp': '',
    # Роботодатель ИП
    #'IPExp':'1',
    # 'OGRNIPExp':'',
    # 'INNIPExp': '772071873841',
    # 'FIOIPExp':'',
    # 'RegionIPExp':'',
    # 'CityIPExp':'',
    # 'StreetIPExp':'',
    # 'HouseIPExp':'',
    # 'BuildIPExp':'',
    # 'BuildingIPExp':'',
    # 'FlatIPExp':'',
    # 'PhoneIPExp':'',

    'zapros': 'Exp',
    'url': billingFLURL
}  # 11
VIFL_External = {
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'VIFL_External': '1',
    'SurName': 'ХРОМОВ',
    'FirstName': 'АЛЕКСАНДР',
    'MiddleName': 'ВАЛЕРИАНОВИЧ',
    'DateOfBirth': '03.08.1969',
    'Seria': '4597',
    'Number': '005229',
    'RegionExp': '45',
    'zapros': 'VIFL_External',
    'url': billingFLURL}  # 12
FR = {'Type': 'Request',
         'WorkingDirectory': WD,
         'Event': '3',
         'FR': '1',
         'SurName': 'ХРОМОВ',
         'FirstName': 'АЛЕКСАНДР',
         'MiddleName': 'ВАЛЕРИАНОВИЧ',
         'DateOfBirth': '03.08.1969',
         'Seria': '4597',
         'Number': '005229',
        'PlaceOfBirth': '123',
         'InfoType': '1',
         'zapros': 'FR',
    'url': billingFLURL}  # 10



ulFNST = {'Type': 'Request',
          'WorkingDirectory': WD,
          'Event': '1',
          'FNST': '1',
          'OGRN': '1177746172790',
          #'INN': '3213213211',
          'zapros': 'FNST',
        'url': billingULURL}  # 0
ulFNSA = {'Type': 'Request',
          'WorkingDirectory': WD,
          'Event': '1',
          'FNSA': '1',
          'OGRN': '1177746172790',
          'zapros': 'FNSA',
        'url': billingULURL}  # 1
ulGIBDD = {'Type': 'Request',
           'WorkingDirectory': WD,
           'Event': '1',
           'GIBDD': '1',
           'OGRN': '1177746172790',
           'zapros': 'GIBDD',
        'url': billingULURL}  # 2
ulBalans = {'Type': 'Request',
            'WorkingDirectory': WD,
            'Event': '1',
            'Balans': '1',
            'OGRN': '1177746172790',
            'zapros': 'Balans',
        'url': billingULURL}  # 3
ulSVI = {'Type': 'Request',
         'WorkingDirectory': WD,
         'Event': '1',
         'SVI': '1',
         'OGRN': '1177746172790',
         'zapros': 'SVI',
        'url': billingULURL}  # 4
ulBenef = {'Type': 'Request',
           'WorkingDirectory': WD,
           'Event': '1',
           'Benef': '1',
           'OGRN': '1177746172790',
           'zapros': 'Benef',
        'url': billingULURL}  # 5
ulAFF = {'Type': 'Request',
         'WorkingDirectory': WD,
         'Event': '1',
         'AFF': '1',
         'OGRN': '1177746172790' ,
         'zapros': 'AFF',
        'url': billingULURL}  # 6
ulEmployer = {'Type': 'Request',
              'WorkingDirectory': WD,
              'Event': '1',
              'Employer': '1',
              'OGRN': '1137847271924',
              'NameOrg': 'ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ "ДЕТЕЛЬ"',
              'Region': '40',
              'City': 'Санкт-Петербург',
              'Phone': '8129837762',
              'zapros': 'Employer',
        'url': billingULURL}  # 7
ulExtSource = {'Type': 'Request',
               'WorkingDirectory': WD,
               'Event': '1',
               'ExtSource': '1',
               'OGRN': '1026102103466',
               'INN': '',
               'zapros': 'ExtSource',
        'url': billingULURL}  # 8
ulBSUL = {'Type': 'Request',
           'WorkingDirectory': WD,
           'Event': '1',
           'BSUL': '1',
           'OGRN': '1177746172790',
           'zapros': 'BSUL',
        'url': billingULURL}  # 0
ulBSPD = {'Type': 'Request',
             'WorkingDirectory': WD,
             'Event': '1',
             'BSPD': '1',
             'OGRN': '1177746172790',
             'zapros': 'BSPD',
            'url': billingULURL}  # 1
ulSVI = {'Type': 'Request',
            'WorkingDirectory': WD,
            'Event': '1',
            'SVI': '1',
            'OGRN': '1177746172790',
            'zapros': 'SVI',
        'url': billingULURL}
ulBSR = {
    'Type': 'Request',
    'Event': '9',
    'BSR': '1',
    'WorkingDirectory': WD,
    # -----------------------------------------------------------------------------------------------------------------------
    'NameOrg': 'ГАЛС ПРОМ',
    'OGRN': '1133703000683',#'',
    'INN': '3703047495',
    'KPP': '000000000',
    'RegistrationDate': '07.10.2013',
    'authCapital': '0',
    'OKVED': '01',
    # -----------------------------------------------------------------------------------------------------------------------
    'addressList[0][addressType]': 'L',
    'addressList[0][Region]': '37',
    'addressList[0][City]': 'Кинешма',
    'addressList[0][Street]': 'Ивана Виноградова',
    'addressList[0][House]': '2',
    'addressList[0][Build]': 'г',  ###
    'addressList[0][Building]': '1',  ###
    'addressList[0][Office]': '',  ###

    # 'contactInfo[0][Phone]': '4958555668',
    # 'contactInfo[0][Fax]': '4959555668',  ###
    # # Директор
    # 'leaderInfoList[0][LeaderCode]': 'L1',
    # 'leaderInfoList[0][SurName]': 'Ахметов',
    # 'leaderInfoList[0][FirstName]': 'Фаиль',
    # 'leaderInfoList[0][MiddleName]': 'Сагитович',  ###
    # 'leaderInfoList[0][DateOfBirth]': '22.01.1963',
    # 'leaderInfoList[0][Seria]': '8097',
    # 'leaderInfoList[0][Number]': '011436',
    # ФЛ Участники
    # 'participantInfoList[0][ParticipantCode]': 'P1',
    # 'participantInfoList[0][SurName]': 'Карпов',
    # 'participantInfoList[0][FirstName]': 'Сергей',
    # 'participantInfoList[0][MiddleName]': 'Владимирович',  ###
    # 'participantInfoList[0][DateOfBirth]': '24.06.1974',
    # 'participantInfoList[0][Seria]': '8004',
    # 'participantInfoList[0][Number]': '181211',
    # 'participantInfoList[0][AuthCapShare]': '54000',
    # # ЮЛ Участники
    # 'legalInfoList[0][OGRN]': '1087746801130',
    # 'legalInfoList[0][AuthCapShare]': '16000',
    # -----------------------------------------------------------------------------------------------------------------------
    'addressList[1][addressType]': 'F',
    'addressList[1][Region]': '37',
    'addressList[1][City]': 'Кинешма',
    'addressList[1][Street]': 'Ивана Виноградова',
    'addressList[1][House]': '2',
    'addressList[1][Build]': 'г',
    'addressList[1][Building]': '1',
    'addressList[1][Office]': '',

    'contactInfo[1][Phone]': '4933155440',
    'contactInfo[1][Fax]': '',

    # 'leaderInfoList[1][LeaderCode]': 'L2',
    # 'leaderInfoList[1][SurName]': 'ЛИЧАГИН',
    # 'leaderInfoList[1][FirstName]': 'ПАВЕЛ',
    # 'leaderInfoList[1][MiddleName]': 'АНАТОЛЬЕВИЧ',
    # 'leaderInfoList[1][DateOfBirth]': '10.10.1965',
    # 'leaderInfoList[1][Seria]': '4321',
    # 'leaderInfoList[1][Number]': '654321',
    #
    # 'participantInfoList[1][ParticipantCode]': 'P1',
    # 'participantInfoList[1][SurName]': 'ЛИЧАГИН',
    # 'participantInfoList[1][FirstName]': 'ПАВЕЛ',
    # 'participantInfoList[1][MiddleName]': '',
    # 'participantInfoList[1][DateOfBirth]': '10.10.1970',
    # 'participantInfoList[1][Seria]': '1234',
    # 'participantInfoList[1][Number]': '123456',
    # 'participantInfoList[1][AuthCapShare]': '1000',
    #
    # 'legalInfoList[1][OGRN]': '1027700107599',
    # 'legalInfoList[1][AuthCapShare]': '15000',
    'zapros': 'BSR',
        'url': billingULURL
}



ipIPT = {'Type': 'Request',
         'WorkingDirectory': WD,
         'Event': '2',
         'IPT': '1',
         #'OGRNIP' : '312751502300034',
         'INNIP': '231400212630',
         'zapros': 'IPT'}  # 0
ipIPA = {'Type': 'Request',
         'WorkingDirectory': WD,
         'Event': '2',
         'IPA': '1',
         'OGRNIP': '312751502300034',
         'zapros': 'IPA'}  # 1
ipExtendedIP = {'Type': 'Request',
                'WorkingDirectory': WD,
                'Event': '2',
                'ExtendedIP': '1',
                'OGRNIP': '312751502300034',
                #'INNIP' : '',
                'zapros': 'ExtendedIP'}  # 2
ipEmployer = {'Type': 'Request',
              'WorkingDirectory': WD,
              'Event': '2',
              'Employer': '1',
              #'OGRNIP': '312751502300034',
              'INNIP': '231293645637',
              'FIO': 'ИП Коровников Алексей Валерьевич',
              'Region': '03',
              'City': 'Выселки',
              'Street': '',
              'House': '',
              'Flat': '',
              'Phone': '9034548390',
              'zapros': 'Employer'
              }  # 3
ipExtSource = {'Type': 'Request',
               'WorkingDirectory': WD,
               'Event': '2',
               'ExtSource': '1',
               'OGRNIP': '312751502300034',
               'zapros': 'ExtSource'}  # 4
ipIDIP = {'Type': 'Request',
         'WorkingDirectory': WD,
         'Event': '2',
         'IDIP': '1',
         #'OGRNIP' : '312751502300034',
         #'INNIP': '231400212630',
           "SurName": "ИВАНОВ",
           "FirstName": "ВЛАДИМИР",
           "MiddleName": "АЛЕКСАНДРОВИЧ",
            "RegionExp": "45",
         'zapros': 'IDIP'} # 5
ipBIP = {
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '7',
    'BIP': '1',
    'SurName': 'ХРОМОВ',
    'FirstName': 'АЛЕКСАНДР',
    'MiddleName': 'ВАЛЕРИАНОВИЧ',
    'DateOfBirth': '03.08.1969',
    'Seria': '4597',
    'Number': '005226',
    'OGRNIP': '312774618000575',
    'INNExp': '770404319004',
    'RegionExp': '45',
    'CityExp': 'МОСКВА',
    'StreetExp': 'ПОЖАРСКИЙ',
    'HouseExp': '15',
    'BuildExp': '',
    'BuildingExp': '',
    'FlatExp': '6',
    'PhoneExp': '4956950322',
    # Или Временная регистрация
    #     'RegionExpTmp':'',
    #     'CityExpTmp':'',
    #     'StreetExpTmp':'',
    #     'HouseExpTmp':'',
    #     'BuildExpTmp':'',
    #     'BuildingExpTmp':'',
    #     'FlatExpTmp':'',
    'zapros': 'BIP'
}  # 0




IDADDRESS = {
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '8',
    'IDADDRESS': '1',
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'ПОЖАРСКИЙ',
    'HouseExp': '15',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '6',
    'zapros': 'IDADDRESS',
    'url': billingADURL
}



PASP_UPassporta = {'Type': 'Request',
                   'WorkingDirectory': WD,
                   'Event': '4',
                   'UPassporta': '1',
                   'Seria': '4500',
                   'Number': '375473',
                   'zapros': 'UPassporta',
                   'url': billingPASPURL}  # 0
PASP_PPFMS = {'Type': 'Request',
              'WorkingDirectory': WD,
              'Event': '4',
              'PPFMS': '1',
              'Seria': '4500',
              'Number': '375473',
              'zapros': 'PPFMS',
              'url': billingPASPURL}  # 1

GIBDD_TS = {'Type': 'Request',
            'WorkingDirectory': WD,
            'Event': '6',
            'TS': '1',
            #'GosNumber': 'M775XY27',
            'VIN': 'WDD2040491A652976',
            'zapros': 'TS',
            'url': billingGIBDDURL
            }  # 0
GIBDD_BCars = {'Type': 'Request',
               'WorkingDirectory': WD,
               'Event': '6',
               'BCars': '1',
               'GosNumber': 'M775XY27',
               # 'VIN': '',
               'zapros': 'BCars',
            'url': billingGIBDDURL
               } # 1
GIBDD_SCars = {'Type': 'Request',
               'WorkingDirectory': WD,
               'Event': '6',
               'SCars': '1',
               'GosNumber': 'M775XY27',
               # 'VIN': '',
               'zapros': 'SCars',
            'url': billingGIBDDURL
               } # 2



  # 0

FL = [
    IDFL,
    CASBO,
    CASBR,
    Raiting,
    RaitingR,
    Raiting_2,
    Raiting_2R,
    Raiting_3R,
    Raiting_4R,
    # FLFR,
    AFF,
    CKKI,
    SVI,
    Exp,
    VIFL_External,
]
UL = [ulFNST,
      ulFNSA,
      # ulULGIBDD,
      ulBalans,
      ulSVI,
      ulBenef,
      ulAFF,
      ulEmployer,
      ulExtSource,
    ulBSUL,
    ulBSPD,
    ulSVI,
    ulBSR

      ]  # 0
IP = [ipIPT,
      ipIPA,
      ipExtendedIP,
      ipEmployer,
      ipExtSource,
        ipIDIP,
    ipBIP
      ]  # 1
AD = [
    IDADDRESS,]
PASP = [
    PASP_UPassporta,
    PASP_PPFMS,
]
GIBDD = [
    GIBDD_TS,
    GIBDD_BCars,
    GIBDD_SCars,
]




Services = [UL,
            IP,
            FL,
            PASP,
            # GIBDD,
         ]


def login():

    post={
                    'Type': 'Login',
                    'Login': LOGIN,
                    'Password': PASSWORD}
    rPOST = S.post(loginURL,data=post, )
    #print(rPOST.text)
    try:
        lx = html.fromstring(rPOST.content)
        WD = lx.xpath('//sid/text()')[0]
        print('получил WD ' + str(WD))
        if WD == '':
            print('не получил WD')
        return WD
    except Exception as e:
        print(e)



def billingType_COUNT():
    with open('C:\Projects_Python3-5-2\\3-5-2\Morda\ADMINKA\\admin data\\admin_data.json', encoding='utf-8') as file:
        line = json.load(file,)
        line['user[billingType]'] = 'COUNT'
        #line['user[blockingReason]'] = '<p>парапапапа</p>'
        print(line)
        post = line
        print(pushURL)
        r = S.post(pushURL, data=post)
        print(r.text)

def logout():
    post = {
        'Type': 'Logout',
        'WorkingDirectory': WD,
    }
    r = S.post(URL + 'logout', data=post )
    xmlBODY = (r.content)
    lx = html.fromstring(xmlBODY)
    ANS = lx.xpath('//text()')[3]
    print('\n')
    print('LOGOUT ' + str(ANS))

def getBilling(billingURL):
    try:

        rGET = S.get(billingURL)

        # parsed = json.loads(rGET.text)['billing']  # str(r.json()["result"])
        # parsed = json.dumps(parsed, indent=4, sort_keys=True, ensure_ascii=False)
        # print(parsed)
        for i in rGET.json()['billing']:
            subsystemBilling[i['code']] = i['requestCount']

        # print(rGET.json()['billing'][11]['title'])
        # print(rGET.json()['billing'][11]['requestCount'])
        # l = []


        # for n,m in subsystemBilling.items():
        #     print('%s : %s' %(n,m))


        #     l.append([n,m])
        # df = pd.DataFrame(l)
        # result = df.to_string(index=True, header=False)
        # print(result)

        return subsystemBilling
    except:
        print(subsystemBilling[i['code']])

def request(requestURL, WD, service):

    service['WorkingDirectory'] = WD
    r = S.post(requestURL,data=service)
    STATUS = r.status_code
    try:
        RN = r.json()['request']['id']
        re1 = "[A-Z0-9]{8}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{12}"
        rg = re.compile(re1,re.IGNORECASE|re.DOTALL)
        rg = rg.search(RN)

        if rg: pass
            #print(service['zapros'] + ' - ' + 'RN: ' + str(RN))
        else:
            print(service['zapros'] + ' - ' + 'ERROR: ' + RN + '\n')
            ERRORS.append(service['zapros'] + ' - ' + 'ERROR: ' + RN)
            ERRORS.append('---------------------------')
        RNs[RN]= service


        if RN == 'ERROR_VALIDATION_WORKINGDIRECTORY' or WD == 'ERROR_VALIDATION_WORKINGDIRECTORY':
            return 'err'
        else:
            return (STATUS, r.text)
    except:
        print(r.text)

def countBilling(billingURL, service,requestURL):
    STATUS, text = '',''

    billing0 = getBilling(billingURL)[service['zapros']]
    print(billing0)
    try:
        STATUS, text = request(requestURL, WD, service)
    except:
        print(request(requestURL, WD, service))
    billing1 = getBilling(billingURL)[service['zapros']]
    billing = billing0 - billing1
    print(billing1)
    if billing == 1: return ('%s - OK' %(service['zapros']))
    else: return ('%s - notOK   Status - %s     Trext:%s' %(service['zapros'], STATUS, text) )




WD = login()

billingType_COUNT()

for service in FL:
    print(countBilling(billingFLURL, service, requestFLURL))

for service in UL:
    print(countBilling(billingULURL, service, requestULURL))

for service in IP:
    print(countBilling(billingIPURL, service, requestIPURL))

for service in AD:
    print(countBilling(billingADURL, service, requestADURL))

for service in PASP:
    print(countBilling(billingPASPURL, service, requestPASPURL))

for service in GIBDD:
    print(countBilling(billingGIBDDURL, service, requestGIBDDURL))






# i = 0
# while i < 20:
#     service = Exp
#     print(countBilling(billingFLURL, service, requestFLURL))
#     i += 1
#     sleep(1)

logout()