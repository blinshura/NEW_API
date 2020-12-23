import json
import random
from datetime import datetime

from lxml import etree
from time import sleep
import requests
from bs4 import BeautifulSoup
from lxml import html
import re
import urllib3
import ssl


urllib3.disable_warnings()





# ips1 'http://127.0.0.1:3337/api'
# ips2 'http://127.0.0.1:3338/api'
# vips1 'http://127.0.0.1:3331/api'


URL = 'http://vips1:3777/api' #'http://127.0.0.1:3331/api' - випс через stunnel  #ips1: 192.168.0.118:450  vips1: 192.168.0.135:3777
LOGIN = 'demo'#'demo' #'Svetka' #'ander_автомат'
PASSWORD = 'demo'#'Gfd!1qaz40' #'153759' #'687dd78R'
R = requests.Session()
Exceptions = []
ERRORS = []
HEADERS={
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'}
WD = ''
RNs = {}



BSUL_RASH = {
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
    'zapros': 'BSUL-Rash'
}  # 0

# сервисы
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
    'zapros': 'IDADDRESS'
}

IDUL = {'Type': 'Request',
          'WorkingDirectory': WD,
          'Event': '1',
          'IDUL': '1',
          'OGRN': '',
          'INN': '',
          'NZA': '10150000014',
          'zapros': 'IDUL'}
ULFNST = {'Type': 'Request',
          'WorkingDirectory': WD,
          'Event': '1',
          'FNST': '1',
          'OGRN': '1027700272148',
          'INN': '',
          #'NZA': '10180002866',
          'zapros': 'UL-FNST'}  # 0
ULFNSA = {'Type': 'Request',
          'WorkingDirectory': WD,
          'Event': '1',
          'FNSA': '1',
          'OGRN': '1177746172790',
          'zapros': 'UL-FNSA'}  # 1
ULGIBDD = {'Type': 'Request',
           'WorkingDirectory': WD,
           'Event': '1',
           'GIBDD': '1',
           'OGRN': '1177746172790',
           'zapros': 'UL-GIBDD'}  # 2
ULBalans = {'Type': 'Request',
            'WorkingDirectory': WD,
            'Event': '1',
            'Balans': '1',
            #'OGRN': '1177746172790',
            'INN': '7704218694',
            'Year': '2012',
            'zapros': 'UL-Balans'}  # 3
ULSVI = {'Type': 'Request',
         'WorkingDirectory': WD,
         'Event': '1',
         'SVI': '1',
         'OGRN': '1177746172790',
         'zapros': 'UL-SVI'}  # 4
ULBenef = {'Type': 'Request',
           'WorkingDirectory': WD,
           'Event': '1',
           'Benef': '1',
           'OGRN': '1177746172790',
           'zapros': 'UL-Benef'}  # 5
ULAFF = {'Type': 'Request',
         'WorkingDirectory': WD,
         'Event': '1',
         'AFF': '1',
         'OGRN': '1177746172790' ,
         'zapros': 'UL-AFF'}  # 6
ULEmployer = {'Type': 'Request',
              'WorkingDirectory': WD,
              'Event': '1',
              'Employer': '1',
              'OGRN': '1137847271924',
              'NameOrg': 'ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ "ДЕТЕЛЬ"',
              'Region': '40',
              'City': 'Санкт-Петербург',
              'Phone': '8129837762',
              'zapros': 'UL-Employer'}  # 7
ULExtSource = {'Type': 'Request',
               'WorkingDirectory': WD,
               'Event': '1',
               'ExtSource': '1',
               'OGRN': '1026102103466',
               'INN': '',
               'zapros': 'UL-ExtSource'}  # 8
ULRaiting = {'Type': 'Request',
             'WorkingDirectory': WD,
             'Event': '1',
             'Raiting': '1',
             'OGRN': '1026102103466',
            'INN': '',
             'zapros': 'ULRaiting'}

IPIPT = {'Type': 'Request',
         'WorkingDirectory': WD,
         'Event': '2',
         'IPT': '1',
         #'OGRNIP' : '312751502300034',
         'INNIP': '231400212630',
         'zapros': 'IPIPT'}  # 0
IPIPA = {'Type': 'Request',
         'WorkingDirectory': WD,
         'Event': '2',
         'IPA': '1',
         'OGRNIP': '312751502300034',
         'zapros': 'IPIPA'}  # 1
IPExtendedIP = {'Type': 'Request',
                'WorkingDirectory': WD,
                'Event': '2',
                'ExtendedIP': '1',
                'OGRNIP': '312751502300034',
                #'INNIP' : '',
                'zapros': 'IP-ExtendedIP'}  # 2
IPEmployer = {'Type': 'Request',
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
              'zapros': 'IP-Employer'
              }  # 3
IPExtSource = {'Type': 'Request',
               'WorkingDirectory': WD,
               'Event': '2',
               'ExtSource': '1',
               #'OGRNIP': '312751502300034',
               'INNIP': '526019668776',
               'zapros': 'IP-ExtSource'}  # 4
IDIP = {'Type': 'Request',
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
           'zapros': 'FL-GIBDD'}  # 0
FLCASBO = {'Type': 'Request',
           'WorkingDirectory': WD,
           'Event': '3',
           'CASBO': '1',
           'SurName': 'ХРОМОВ',
           'FirstName': 'АЛЕКСАНДР',
           'MiddleName': 'ВАЛЕРИАНОВИЧ',
           'DateOfBirth': '03.08.1969',
           'Seria': '4597',
           'Number': '005229',
           'zapros': 'FL-CASBO'}  # 1
FLCASBR = {'Type': 'Request',
           'WorkingDirectory': WD,
           'Event': '3',
           'CASBR': '1',
           'SurName': 'ХРОМОВ',
           'FirstName': 'АЛЕКСАНДР',
           'MiddleName': 'ВАЛЕРИАНОВИЧ',
           'DateOfBirth': '03.08.1969',
           'Seria': '4597',
           'Number': '005229',
           'zapros': 'FL-CASBR'}  # 2
FLRaiting = {'Type': 'Request',
             'WorkingDirectory': WD,
             'Event': '3',
             'Raiting': '1',
             'SurName': 'ХРОМОВ',
             'FirstName': 'АЛЕКСАНДР',
             #'MiddleName': 'ВАЛЕРИАНОВИЧ',
             'DateOfBirth': '03.08.1969',
             'Seria': '4597',
             'Number': '005229',
             'IssueDate': '03.08.1969',
             'zapros': 'FL-Raiting'}  # 3
FLRaitingR = {'Type': 'Request',
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
              'zapros': 'FL-RaitingR'}  # 4
FLRaiting_2 = {'Type': 'Request',
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
               'zapros': 'FL-Raiting_2'}  # 5
FLRaiting_2R = {'Type': 'Request',
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
                'zapros': 'FL-Raitin_2R'}  # 6
FLRaiting_3R = {'Type': 'Request',
                'WorkingDirectory': WD,
                'Event': '3',
                'Raiting_3R': '1',
                'SurName': 'ХРОМОВ',
                'FirstName': 'АЛЕКСАНДР',
                #'MiddleName': 'ВАЛЕРИАНОВИЧ',
                'DateOfBirth': '03.08.1969',
                'Seria': '4597',
                'Number': '005229',
                #'IssueDate': '03.08.1969',
                'zapros': 'FL-Raitin_3R'}
FLRaiting_4R = {'Type': 'Request',
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
                'CityExp': u'МОСКВА',
                'StreetExp': u'Зои и Александра Космодемьянских',
                'HouseExp': '33',
                'BuildExp': '',  # или
                'BuildingExp': '',
                'FlatExp': '30',
                'zapros': 'FL-Raitin_4R'}
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
#         'zapros': 'FL-FR'}  # 7
FLAFF = {'Type': 'Request',
         'WorkingDirectory': WD,
         'Event': '3',
         'AFF': '1',
         'SurName': 'ХРОМОВ',
         'FirstName': 'АЛЕКСАНДР',
         #'MiddleName': 'ВАЛЕРИАНОВИЧ',
         'DateOfBirth': '03.08.1969',
         'Seria': '4597',
         'Number': '005229',
         'zapros': 'FL-AFF'}  # 8
FLCKKI = {'Type': 'Request',
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
          'zapros': 'FL-CKKI'}  # 9
FLSVI = {'Type': 'Request',
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
         'zapros': 'FL-SVI'}  # 10
FLExp = {
    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
    'SurName': u'Жотин',
    'FirstName': u'Роман',
    'MiddleName': u'Сергеевич',
    'DateOfBirth': '31.07.1983',
    'Seria': '4703',
    'Number': '853404',
    #'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Зои и Александра Космодемьянских',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '89263830685',
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

    'zapros': 'FL-Exp'
}  # 11
FLExtSource = {
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'ExtSource': '1',
    'SurName': 'ХРОМОВ',
    'FirstName': 'АЛЕКСАНДР',
    'MiddleName': 'ВАЛЕРИАНОВИЧ',
    'DateOfBirth': '03.08.1969',
    'Seria': '4597',
    'Number': '005229',
    'RegionExp': '45',
    'zapros': 'FL-ExtSource'}  # 12
FLFR = {'Type': 'Request',
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
         'zapros': 'FLFR'}  # 10
FLBSFL = {'Type': 'Request',
         'WorkingDirectory': WD,
         'Event': '3',
         'BSFL': '1',
          'SurName': 'ХРОМОВ',
          'FirstName': 'АЛЕКСАНДР',
          #'MiddleName': 'ВАЛЕРИАНОВИЧ',
          'DateOfBirth': '13.04.2006',
          'Seria': '4597',
          'Number': '005229',
        #'IssueDate': '03.08.1969',
        #'INNExp': '770404319004',
        'zapros': 'FL-BSFL'
          }

PASP_UPassporta = {'Type': 'Request',
                   'WorkingDirectory': WD,
                   'Event': '4',
                   'UPassporta': '1',
                   'Seria': '4500',
                   'Number': '375473',
                   'zapros': 'Pasp-UPassporta'}  # 0
PASP_PPFMS = {'Type': 'Request',
              'WorkingDirectory': WD,
              'Event': '4',
              'PPFMS': '1',
              'Seria': '4500',
              'Number': '375473',
              'zapros': 'Pasp-PPFMS'}  # 1

BSUL_BS = {'Type': 'Request',
           'WorkingDirectory': WD,
           'Event': '1',
           'BS': '1',
           'OGRN': '1177746172790',
           'zapros': 'BSUL-BS'}  # 0
BSUL_BSPD = {'Type': 'Request',
             'WorkingDirectory': WD,
             'Event': '1',
             'BSPD': '1',
             'OGRN': '1177746172790',
             'zapros': 'BSUL-BSPD'}  # 1
BSUL_SVI = {'Type': 'Request',
            'WorkingDirectory': WD,
            'Event': '1',
            'SVI': '1',
            'OGRN': '1177746172790',
            'zapros': 'BSUL-SVI'}  # 2

GIBDD_TS = {'Type': 'Request',
            'WorkingDirectory': WD,
            'Event': '6',
            'TS': '1',
            'GosNumber': 'M775XY27',
            # 'VIN': '',
            'zapros': 'GIBDD-TS'
            }  # 0
GIBDD_BCars = {'Type': 'Request',
               'WorkingDirectory': WD,
               'Event': '6',
               'BCars': '1',
               'GosNumber': 'M775XY27',
               # 'VIN': '',
               'zapros': 'GIBDD-BCars'
               } # 1
GIBDD_SCars = {'Type': 'Request',
               'WorkingDirectory': WD,
               'Event': '6',
               'SCars': '1',
               'GosNumber': 'M775XY27',
               # 'VIN': '',
               'zapros': 'GIBDD-SCars'
               } # 2

BSIP_BIP = {
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '7',
    'BIP': '1',
    'SurName': 'ХРОМОВ',
    'FirstName': 'АЛЕКСАНДР',
    'MiddleName': 'ВАЛЕРИАНОВИЧ',
    'DateOfBirth': '14.04.2006',
    'Seria': '4597',
    'Number': '005220',
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
    'zapros': 'PSIP-BIP'
}  # 0

IDFL = {
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '8',
    'IDFL': '1',

     # 'SurName': 'Мушанова',
     # 'FirstName': 'Евгения',
     # 'MiddleName': 'Васильевна',
    # 'DateOfBirth': '30.10.1983',
    'Seria': '4004',
    'Number': '946593',
    # 'Address': '40 САНКТ ПЕТЕРБУРГ ВОЗНЕСЕНСКИЙ 34 1',
    #'Phone': '1',
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
    'zapros': 'IDFL'
} # 0
UL = [ULFNST,
      ULFNSA,
      # ULGIBDD,
      ULBalans,
      ULSVI,
      ULBenef,
      ULAFF,
      ULEmployer,
      ULExtSource,
    ULRaiting
      ]  # 0
IP = [IPIPT,
      IPIPA,
      IPExtendedIP,
      IPEmployer,
      IPExtSource,
        IDIP
      ]  # 1
FL = [
    # FLGIBDD,
    FLCASBO,
    FLCASBR,
    FLRaiting,
    FLRaitingR,
    FLRaiting_2,
    FLRaiting_2R,
FLRaiting_3R,
FLRaiting_4R,
    # FLFR,
    FLAFF,
    FLCKKI,
    FLSVI,
    FLExp,
    FLExtSource,
FLBSFL,
]
PASP = [
    PASP_UPassporta,
    PASP_PPFMS,
]
BSUL = [
    BSUL_BS,
    BSUL_BSPD,
    BSUL_SVI,
]
GIBDD = [
    GIBDD_TS,
    GIBDD_BCars,
    GIBDD_SCars,
]
BSIP = [
    BSIP_BIP,
]
ID_FL = [
    IDFL
]
BS_R = [
   BSUL_RASH
]

Services = [UL,
            IP,
            FL,
            PASP,
            BSUL,
            # GIBDD,
            BSIP,
            ID_FL,
            BS_R]

def login():
    login_start_time = datetime.now()

    post={
                    'Type': 'Login',
                    'Login': LOGIN,
                    'Password': PASSWORD}
    r = R.post(URL,data=post, headers=HEADERS,  verify=False) #'C:\Soft\Тестирование\КриптоПро\ssl.croinform.ru.cer'
    #print(r.text)
    lx = html.fromstring(r.content)
    WD = lx.xpath('//text()')[1]
    print('WD ' + str(WD))

    login_end_time = datetime.now()
    login_total_time = login_end_time - login_start_time
    #print('login_total_time ' + str(login_total_time))
    with open('c:\\log_API.txt','a') as log:
        log.write(str(login_total_time) + ' ' + 'login' + ' ' + WD + '\n')
    return WD

def request(WD,service):
    request_start_time = datetime.now()
    service['WorkingDirectory'] = WD
    r = requests.post(URL,data=service,headers=HEADERS, verify=False,)
    lx = html.fromstring(r.content)
    RN = lx.xpath('//text()')[1]
    re1 = "[A-Z0-9]{8}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{12}"
    rg = re.compile(re1,re.IGNORECASE|re.DOTALL)
    rg = rg.search(RN)
    if rg:
        #print('RN ' + str(RN))
        print(service['zapros'] + ' - ' + 'RN: ' + str(RN) + '\n')
    else:
        print(RN)
        print(service['zapros'] + ' - ' + 'ERROR: ' + RN + '\n')
        ERRORS.append(service['zapros'] + ' - ' + 'ERROR: ' + RN)
        #ERRORS.append(RN)
        ERRORS.append('---------------------------')
    RNs[RN]= service['zapros']

    request_end_time = datetime.now()
    request_total_time = request_end_time - request_start_time
    #print('request_total_time ' + str(request_total_time))
    with open('c:\\log_API.txt', 'a') as log:
        log.write(str(request_total_time) + ' ' + 'request' + ' ' + RN + '\n')

    if RN == 'ERROR_VALIDATION_WORKINGDIRECTORY' or WD == 'ERROR_VALIDATION_WORKINGDIRECTORY':
        return 'err'
    else:
        return RN

def response(WD, RN, service):
    response_start_time = datetime.now()
    StatusANS = '3'
    StatisticANS = ''
    tryes = 9999
    while StatusANS == '3' and tryes >= 1:

        post = {'Type': 'Answer',
                'WorkingDirectory': WD,
                'RequestNumber': RN,
                'TypeAnswer': 'HV',
                }
        post['RequestNumber'] = RN
        post['WorkingDirectory'] = WD
        r = requests.post(URL, data=post, headers=HEADERS, verify=False,)
        sleep(0.5)


        #print(r.text)





        ANSWER = BeautifulSoup(r.content, 'lxml')

        if ANSWER.findAllNext('statistics') != None:
            StatisticANS = ANSWER.statistics
            StatisticANS = str(StatisticANS)

        if ANSWER.find('statusrequest') !=None:
            StatusANS = ANSWER.statusrequest.text
            StatusANS = str(StatusANS)
        else:
            lx = html.fromstring(r.content)
            print(r.text)
            StatusANS = lx.xpath('//text()')[3]
            StatusANS = str(StatusANS)




        # Очистка ответа
        if StatusANS != '3':


            if '<td>' in str(ANSWER):
                ANSWER = ('  '.join(ANSWER.findAll(text=True)))[41921:-11100]
                print(ANSWER)
        #         for t in ANSWER.find_all('td'):
        #             t = str(t).replace('<td></td>', '\n')
        #             t = t.replace('</td>', '')
        #             t = t.replace('<td>', '')
        #             print(t)

            else:
                ANSWER = ('  '.join(ANSWER.findAll(text=True)))[41921:-11100]
                print(ANSWER)
                # for t in ANSWER.find_all('div'):
                #     if 'script' not in str(t):
                #         t = str(t).replace('</div>', '')
                #         t = t.replace('<div>', '')
                #         t = t.replace('</p>', '')
                #         t = t.replace('<p>', '')
                #         t = t.replace('</li>', '')
                #         t = t.replace('</ol>', '')
                #         t = t.replace('<ol>', '')
                #         t = t.replace('<li>', '')
                #         t = t.replace('<span>', '')
                #         t = t.replace('</span>', '')
                #         print(t)


            #print(StatisticANS)   # ВЫВОДИМ СТАТИСТИКУ!!!!!!!!!!!!!!!!

        if StatusANS == '3': sleep(1)

        print('\n' + 'ANS-' + StatusANS + '  try-' + str(tryes) + '  ' + service['zapros'] + '  ' + RN)
        tryes -= 1
        if StatusANS == '3' and tryes < 1:
            ERRORS.append(service['zapros'])
            ERRORS.append(RN + ' Не дождались ответа')
            ERRORS.append('---------------------------')
            print(' Не дождались ответа')



        errWD = html.fromstring(r.content)
        errWD = errWD.xpath('//text()')[1]
        if errWD == 'ERROR_VALIDATION_WORKINGDIRECTORY':
            return 'err'



    print('-----------------------------------------------------------------------------------------------------------')

    response_end_time = datetime.now()
    response_total_time = response_end_time - response_start_time
    #print('response_total_time ' + str(response_total_time))
    with open('c:\\log_API.txt', 'a') as log:
        log.write(str(response_total_time) + ' ' + 'response'  + ' ' + RN + '\n')

def logout(WD):
    logout_start_time = datetime.now()
    post={
                            'Type': 'Logout',
                            'WorkingDirectory': WD,
                        }
    r = requests.post(URL, data=post, headers=HEADERS,verify=False,)
    xmlBODY = (r.content)
    lx = html.fromstring(xmlBODY)
    ANS = lx.xpath('//text()')[3]
    print('\n')
    print('LOGOUT ' + str(ANS))

    logout_end_time = datetime.now()
    logout_total_time = logout_end_time - logout_start_time
    #print('logout_total_time ' + str(logout_total_time))
    with open('c:\\log_API.txt', 'a') as log:
        log.write(str(logout_total_time) + ' ' + 'logout' + ' ' + RN + '\n')




if __name__ == '__main__':

    try:

        WD = login()

        # ЦИКЛ ПО ВСЕМ СЕРВИСАМ


        # it = 0
        # while it < 1:
        #
        #     for S in Services:
        #         for s in S:
        #             RN = request(WD, s)
        #             while RN == 'err':
        #                 WD = login()
        #                 sleep(3)
        #                 if WD != 'ERROR_VALIDATION_WORKINGDIRECTORY':
        #                     RN = request(WD, s)
        #                     break
        #
        #
        #
        #     for RN, service in RNs.items():
        #         print(RN)
        #         print(service)
        #         resp = response(WD, RN, service)
        #         while resp == 'err':
        #             WD = login()
        #             sleep(3)
        #             if WD != 'ERROR_VALIDATION_WORKINGDIRECTORY':
        #                 resp = response(WD, RN, service)
        #                 break
        #
        #     it+=1



        # ЕДИНИЧНЫЙ ЗАПРОС

        # service = IDFL # IDFL FLBSFL
        # RN = request(WD, service)
        # response(WD, RN, service)


        # НАГРУЗКА ОТВЕТ СРАЗУ

        # service = IDFL  # IDFL BSUL_RASH IPEmployer ULEmployer IDADDRESS BSUL_BS FLExp
        # t = 0
        # while t < 50:
        #     start = datetime.now()
        #     RN = request(WD, service)
        #     while RN == 'err':
        #         WD = login()
        #         sleep(3)
        #         if WD != 'ERROR_VALIDATION_WORKINGDIRECTORY':
        #             RN = request(WD, service)
        #             break
        #     response(WD, RN, service)
        #     print(datetime.now() - start)
        #     t += 1


        # НАГРУЗКА ОТВЕТ ПОТОМ

        service = FLExp # IDFL BSUL_RASH IPEmployer ULEmployer IDADDRESS BSUL_BS FLExp
        t = 0
        with open ('C:\Projects_Python3-5-2\\3-5-2\API\FILES\\40FL.json',encoding='utf-8')as file:
            jFile = json.load(file)


        while t < 400:
            jRandom = random.choice(jFile)
            print(jRandom)

            service['SurName'] = jRandom['SurName']
            service['FirstName'] = jRandom['FirstName']
            service['MiddleName'] = jRandom['MiddleName']
            service['DateOfBirth'] = jRandom['DateOfBirth']
            service['Seria'] = jRandom['Seria']
            service['Number'] = jRandom['Number']

            RN = request(WD, service)
            while RN == 'err':
                WD = login()
                sleep(3)
                if WD != 'ERROR_VALIDATION_WORKINGDIRECTORY':
                    RN = request(WD, service)
                    break
            t += 1
            sleep(3)
        with open(r'C:\Projects_Python3-5-2\3-5-2\API\FILES\RNs.txt', 'w') as f:
            for i in RNs:
                f.write(i + '\n')
        for Rn in RNs.keys():
            response(WD, Rn, service)






        logout(WD)

        print(Exceptions)
        print('ERRORS:')
        for i in ERRORS:
            print(i)

    except Exception as e:
        print(e)


