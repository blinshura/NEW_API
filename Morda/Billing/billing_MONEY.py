import json

import re
from time import sleep

import requests
from lxml import html
import pandas as pd

URL = 'http://ips1:3080/'#'http://127.0.0.1:3336/' #http://vips1/ #https://ips3:888/ #http://127.0.0.1:3333/
loginURL = URL + 'login'
billingURL = URL + 'api/billing/'
requestURL = URL + 'api/request/'
pushURL = URL +  'admin/api/user/info'

LOGIN = 'demo'#'demo' #'Svetka' #'ander_автомат'
PASSWORD = 'Gfd!1qaz40'#'Gfd!1qaz40' #'153759' #'687dd78R'

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


WD = ''
RN = ''
subsystemBilling = {}
ERRORS = []
RNs = {}
S = requests.Session()
limitCurrent = ''




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
    'billingURL': billingFLURL,
    'requestURL': requestFLURL,
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

           'billingURL': billingFLURL,
           'requestURL': requestFLURL,
           }  # 0
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

    'billingURL': billingFLURL,
    'requestURL': requestFLURL,} # 1
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

    'billingURL': billingFLURL,
    'requestURL': requestFLURL,} # 2
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

    'billingURL': billingFLURL,
    'requestURL': requestFLURL,} # 3
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

    'billingURL': billingFLURL,
    'requestURL': requestFLURL,} # 4
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

    'billingURL': billingFLURL,
    'requestURL': requestFLURL,}  # 5
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

    'billingURL': billingFLURL,
    'requestURL': requestFLURL,} # 6
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

    'billingURL': billingFLURL,
    'requestURL': requestFLURL,}
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

    'billingURL': billingFLURL,
    'requestURL': requestFLURL,}
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
#
#     'billingURL': billingFLURL,
#     'requestURL': requestFLURL,}  # 7
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

       'billingURL': billingFLURL,
       'requestURL': requestFLURL,
       }  # 8
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

    'billingURL': billingFLURL,
    'requestURL': requestFLURL,}  # 9
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

    'billingURL': billingFLURL,
    'requestURL': requestFLURL,}  # 10
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

    'billingURL': billingFLURL,
    'requestURL': requestFLURL,
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

    'billingURL': billingFLURL,
    'requestURL': requestFLURL,}  # 12
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

    'billingURL': billingFLURL,
    'requestURL': requestFLURL,}  # 10



ulFNST = {'Type': 'Request',
          'WorkingDirectory': WD,
          'Event': '1',
          'FNST': '1',
          'OGRN': '1177746172790',
          #'INN': '3213213211',
          'zapros': 'FNST',

    'billingURL': billingULURL,
    'requestURL': requestULURL,}  # 0
ulFNSA = {'Type': 'Request',
          'WorkingDirectory': WD,
          'Event': '1',
          'FNSA': '1',
          'OGRN': '1177746172790',
          'zapros': 'FNSA',
            'billingURL': billingULURL,
    'requestURL': requestULURL,}  # 1
ulGIBDD = {'Type': 'Request',
           'WorkingDirectory': WD,
           'Event': '1',
           'GIBDD': '1',
           'OGRN': '1177746172790',
           'zapros': 'GIBDD',
            'billingURL': billingULURL,
    'requestURL': requestULURL,}  # 2
ulBalans = {'Type': 'Request',
            'WorkingDirectory': WD,
            'Event': '1',
            'Balans': '1',
            'OGRN': '1177746172790',
            'zapros': 'Balans',
            'billingURL': billingULURL,
    'requestURL': requestULURL,}  # 3
ulSVI = {'Type': 'Request',
         'WorkingDirectory': WD,
         'Event': '1',
         'SVI': '1',
         'OGRN': '1177746172790',
         'zapros': 'SVI',
            'billingURL': billingULURL,
    'requestURL': requestULURL,}  # 4
ulBenef = {'Type': 'Request',
           'WorkingDirectory': WD,
           'Event': '1',
           'Benef': '1',
           'OGRN': '1177746172790',
           'zapros': 'Benef',
            'billingURL': billingULURL,
    'requestURL': requestULURL,}  # 5
ulAFF = {'Type': 'Request',
         'WorkingDirectory': WD,
         'Event': '1',
         'AFF': '1',
         'OGRN': '1177746172790' ,
         'zapros': 'AFF',
            'billingURL': billingULURL,
    'requestURL': requestULURL,}  # 6
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
            'billingURL': billingULURL,
    'requestURL': requestULURL,}  # 7
ulExtSource = {'Type': 'Request',
               'WorkingDirectory': WD,
               'Event': '1',
               'ExtSource': '1',
               'OGRN': '1026102103466',
               'INN': '',
               'zapros': 'ExtSource',
            'billingURL': billingULURL,
    'requestURL': requestULURL,}  # 8
ulBSUL = {'Type': 'Request',
           'WorkingDirectory': WD,
           'Event': '1',
           'BSUL': '1',
           'OGRN': '1177746172790',
           'zapros': 'BSUL',
            'billingURL': billingULURL,
    'requestURL': requestULURL,}  # 0
ulBSPD = {'Type': 'Request',
             'WorkingDirectory': WD,
             'Event': '1',
             'BSPD': '1',
             'OGRN': '1177746172790',
             'zapros': 'BSPD',
                'billingURL': billingULURL,
    'requestURL': requestULURL,}  # 1
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
            'billingURL': billingULURL,
    'requestURL': requestULURL,
}



ipIPT = {'Type': 'Request',
         'WorkingDirectory': WD,
         'Event': '2',
         'IPT': '1',
         #'OGRNIP' : '312751502300034',
         'INNIP': '231400212630',
         'zapros': 'IPT',
         'billingURL': billingIPURL,
        'requestURL': requestIPURL,}  # 0
ipIPA = {'Type': 'Request',
         'WorkingDirectory': WD,
         'Event': '2',
         'IPA': '1',
         'OGRNIP': '312751502300034',
         'zapros': 'IPA',
                  'billingURL': billingIPURL,
        'requestURL': requestIPURL,}  # 1
ipExtendedIP = {'Type': 'Request',
                'WorkingDirectory': WD,
                'Event': '2',
                'ExtendedIP': '1',
                'OGRNIP': '312751502300034',
                #'INNIP' : '',
                'zapros': 'ExtendedIP',
                  'billingURL': billingIPURL,
        'requestURL': requestIPURL,}  # 2
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
              'zapros': 'Employer',
                  'billingURL': billingIPURL,
        'requestURL': requestIPURL,
              }  # 3
ipExtSource = {'Type': 'Request',
               'WorkingDirectory': WD,
               'Event': '2',
               'ExtSource': '1',
               'OGRNIP': '312751502300034',
               'zapros': 'ExtSource',
                  'billingURL': billingIPURL,
        'requestURL': requestIPURL,}  # 4
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
         'zapros': 'IDIP',
                  'billingURL': billingIPURL,
        'requestURL': requestIPURL,} # 5
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
    'zapros': 'BIP',
                  'billingURL': billingIPURL,
        'requestURL': requestIPURL,
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
             'billingURL': billingADURL,
        'requestURL': requestADURL,
}



PASP_UPassporta = {'Type': 'Request',
                   'WorkingDirectory': WD,
                   'Event': '4',
                   'UPassporta': '1',
                   'Seria': '4500',
                   'Number': '375473',
                   'zapros': 'UPassporta',
                    'billingURL': billingPASPURL,
                'requestURL': requestPASPURL,}  # 0
PASP_PPFMS = {'Type': 'Request',
              'WorkingDirectory': WD,
              'Event': '4',
              'PPFMS': '1',
              'Seria': '4500',
              'Number': '375473',
              'zapros': 'PPFMS',
                                  'billingURL': billingPASPURL,
                'requestURL': requestPASPURL,}  # 1

GIBDD_TS = {'Type': 'Request',
            'WorkingDirectory': WD,
            'Event': '6',
            'TS': '1',
            #'GosNumber': 'M775XY27',
            'VIN': 'WDD2040491A652976',
            'zapros': 'TS',
                'billingURL': billingGIBDDURL,
                'requestURL': requestGIBDDURL,
            }  # 0
GIBDD_BCars = {'Type': 'Request',
               'WorkingDirectory': WD,
               'Event': '6',
               'BCars': '1',
               'GosNumber': 'M775XY27',
               # 'VIN': '',
               'zapros': 'BCars',
               'billingURL': billingGIBDDURL,
               'requestURL': requestGIBDDURL
               } # 1
GIBDD_SCars = {'Type': 'Request',
               'WorkingDirectory': WD,
               'Event': '6',
               'SCars': '1',
               'GosNumber': 'M775XY27',
               # 'VIN': '',
               'zapros': 'SCars',
               'billingURL': billingGIBDDURL,
               'requestURL': requestGIBDDURL
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




Services = [
            FL,
            UL,
            IP,
            PASP,
            # GIBDD,
         ]

def login():

    post={
                    'Type': 'Login',
                    'Login': LOGIN,
                    'Password': PASSWORD}
    rPOST = S.post(loginURL,data=post, )

    try:
        lx = html.fromstring(rPOST.content)
        WD = lx.xpath('//sid/text()')[0]
        print('получил WD ' + str(WD))
        if WD == '':
            print('не получил WD')
        return WD
    except Exception as e:
        print(e)

def getBilling(billingURL):
    try:

        rGET = S.get(billingURL)
        jGET = rGET.json()
        limitCurrent = jGET['limitCurrent']
        #print(limitCurrent)



        return jGET
    except:
        pass

def request(requestURL, WD, service):

    service['WorkingDirectory'] = WD
    r = S.post(requestURL,data=service)

    try:

        jGET = r.json()

        price = jGET[service['zapros']]

        if RN == 'ERROR_VALIDATION_WORKINGDIRECTORY' or WD == 'ERROR_VALIDATION_WORKINGDIRECTORY':
            return 'err'
        else:
            return (price)

    except Exception as e:
        print(e)




if __name__ == '__main__':
    login()

    for service in Services:
            for s in service:
                billing = getBilling(s['billingURL'])
                first = billing['limitCurrent']
                #print(billing['billing'])
                price = ''
                for f in billing['billing']:
                    if str(f['code']) == str(s['zapros']):
                        price = f['price']


                request(s['requestURL'], WD, s)
                second = getBilling(s['billingURL'])['limitCurrent']

                if int(second) == int(first) - int(price):
                    print('URA  -   ZAPROS:%s   -   PRICE:%s  -   difference:%s' % (s['zapros'], price, int(first)-int(second)))
                else: print('huevo  -   ZAPROS:%s' % s['zapros'])



