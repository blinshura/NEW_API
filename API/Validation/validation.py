from datetime import datetime

from lxml import etree
from time import sleep
import requests
from bs4 import BeautifulSoup
from lxml import html
import re
import urllib3
from poolmanager import PoolManager

urllib3.disable_warnings()
import ssl

#DEBUG
# import requests
# import logging
#
# # These two lines enable debugging at httplib level (requests->urllib3->http.client)
# # You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# # The only thing missing will be the response.body which is not logged.
# try:
#     import http.client as http_client
# except ImportError:
#     # Python 2
#     import httplib as http_client
# http_client.HTTPConnection.debuglevel = 1
#
# # You must initialize logging, otherwise you'll not see debug output.
# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True

# class SslAdapter():
#     def init_poolmanager(self, connections, maxsize, block=False):
#         self.poolmanager = PoolManager(num_pools=connections,
#                                        maxsize=maxsize,
#                                        block=block,
#                                        ssl_version=ssl.PROTOCOL_TLSv1_1,
#                                     )
# s=requests.Session()
# s.mount('https://', SslAdapter())
# s.get('https://google.com', verify=False)

URL = 'http://vips1:3777/api' #'http://ips1:450'  #ips1: 192.168.0.118:450  vips1: 192.168.0.135:3777
LOGIN = 'release'#'demo' #'Svetka' #'ander_автомат'
PASSWORD = 'release'#'Gfd!1qaz40' #'153759' #'687dd78R'
TIMEOUT = 5
R = requests.Session()
Exceptions = []
ERRORS = []
DATA= []
HEADERS={
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'}
WD = ''
RNs = {}



Address_IDFL = {
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '8',
    'IDFL': '1',
    'ERR': 'ERROR_VALIDATION_ADDRESS',
    'service': 'Address_IDFL',

    # 'SurName': 'ПОНАМАРЕВА',
    # 'FirstName': 'ИРИНА',
    # 'MiddleName': 'ЮРЬЕВНА',
    # 'DateOfBirth': '11.01.1966',
    # 'Seria': '4004',
    # 'Number': '946593',
    'Address': 'dafgbad',
    # 'Phone': '8123106658',
    # 'GosNumber': '',
    #'INNIP': '782619098267',
    # 'OGRN': '1056900010375',
    # 'OGRNIP': '',
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

}
BuildExp_ExpFL = {
    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
    'ERR': 'ERROR_VALIDATION_BuildExp',
    'service': 'BuildExp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    #'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '!@#$',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
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
}
BuildOrgExp_ExpFL = {
    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
    'ERR': 'ERROR_VALIDATION_BuildOrgExp',
    'service': 'BuildOrgExp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    #'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '6',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
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
    'OrgExp': '1',
    'OGRNOrgExp': '1154205015832',  # INNOrgExp
    'NameOrgExp': 'ВЕСТА',
    'RegionOrgExp': '32',
    'CityOrgExp': 'КЕМЕРОВО',
    'StreetOrgExp': 'ЛЕНИНА',  # или
    'HouseOrgExp': '128',
    'BuildOrgExp': '!@###$',
    'BuildingOrgExp': '',
    'FlatOrgExp': '709',
    'PhoneOrgExp': '',
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
}
City_ULEmployer = {'Type': 'Request',
              'WorkingDirectory': WD,
              'Event': '1',
              'Employer': '1',
            'ERR': 'ERROR_VALIDATION_City',
               'service': 'City_ULEmployer',

                   'OGRN': '1137847271924',
              'NameOrg': 'ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ "ДЕТЕЛЬ"',
              'Region': '40',
              'City': 'zff',
              'Phone': '8129837762',
              }
CityExp_ExpFL = {
    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
    'ERR': 'ERROR_VALIDATION_CityExp',
'service': 'CityExp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    #'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'asdgf',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
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
    'IPExp':'1',
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
    }
CityExpTmp_ExpFL = {# Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
    'ERR': 'ERROR_VALIDATION_CityExpTmp',
'service': 'CityExpTmp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    #'INNExp': '770404319004',
    # Блок Адрес Постоянный
    # 'RegionExp': '45',
    # 'CityExp': u'asdgf',
    # 'StreetExp': u'Новгородская',
    # 'HouseExp': '33',
    # 'BuildExp': '',  # или
    # 'BuildingExp': '',
    # 'FlatExp': '30',
    # 'PhoneExp': '',
    # Блок Адрес Временный
    'RegionExpTmp':'45',
    'CityExpTmp':('fgh'),
    'StreetExpTmp':('ПОЖАРСКИЙ'),
    'HouseExpTmp':'15',
    'BuildExpTmp':'',
    'BuildingExpTmp':'',
    'FlatExpTmp':'6',
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
    }
CityIPExp_ExpFL = {# Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
    'ERR': 'ERROR_VALIDATION_CityIPExp',
'service': 'CityIPExp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    #'INNExp': '770404319004',
    # Блок Адрес Постоянный
    # 'RegionExp': '45',
    # 'CityExp': u'Москва',
    # 'StreetExp': u'Новгородская',
    # 'HouseExp': '33',
    # 'BuildExp': '',  # или
    # 'BuildingExp': '',
    # 'FlatExp': '30',
    # 'PhoneExp': '',
    # Блок Адрес Временный
    'RegionExpTmp':'45',
    'CityExpTmp':'москва',
    'StreetExpTmp':'ПОЖАРСКИЙ',
    'HouseExpTmp':'15',
    'BuildExpTmp':'',
    'BuildingExpTmp':'',
    'FlatExpTmp':'6',
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
    'IPExp':'1',
    'OGRNIPExp':'',
    'INNIPExp': '772071873841',
    'FIOIPExp':'',
    'RegionIPExp':'',
    'CityIPExp':'sdf',
    'StreetIPExp':'',
    'HouseIPExp':'',
    'BuildIPExp':'',
    'BuildingIPExp':'',
    'FlatIPExp':'',
    'PhoneIPExp':'',
    }
CityOrgExp_ExpFL = {# Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_CityOrgExp',
'service': 'CityOrgExp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
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
    'PhoneExp': '',
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
    'OrgExp': '1',
    'OGRNOrgExp': '1154205015832',  # INNOrgExp
    'NameOrgExp': 'ВЕСТА',
    'RegionOrgExp': '32',
    'CityOrgExp': '!@##',
    'StreetOrgExp': 'ЛЕНИНА',  # или
    'HouseOrgExp': '128',
    'BuildOrgExp': '',
    'BuildingOrgExp': '',
    'FlatOrgExp': '709',
    'PhoneOrgExp': '',
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
    }
DateOfBirth_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_DateOfBirth',
'service': 'DateOfBirth_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '!#@!#!',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
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
    # 'IPExp':'1',
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



}
FIO_IPEmployer = {'Type': 'Request',
              'WorkingDirectory': WD,
              'Event': '2',
              'Employer': '1',
'ERR': 'ERROR_VALIDATION_FIO',
'service': 'FIO_IPEmployer',

              #'OGRNIP': '312751502300034',
              'INNIP': '231293645637',
              'FIO': '!@##!#',
              'Region': '03',
              'City': 'Выселки',
              'Street': '',
              'House': '',
              'Flat': '',
              'Phone': '9034548390',
              }
SURNAME_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_SURNAME',
'service': 'SURNAME_ExpFL',

    'SurName': u'1!#@',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
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
    # 'IPExp':'1',
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

}
FIRSTNAME_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_FIRSTNAME',
'service': 'FIRSTNAME_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'!@##%^',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
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
    # 'IPExp':'1',
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

}
MIDDLENAME_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_MIDDLENAME',
'service': 'MIDDLENAME_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '!#!#@',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
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
    # 'IPExp':'1',
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


}
FIOIPExp_ExpFL = {
    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_FIOIPExp',
'service': 'FIOIPExp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
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
    'IPExp':'1',
    'OGRNIPExp':'',
    'INNIPExp': '772071873841',
    'FIOIPExp':'!$@#@%!#',
    'RegionIPExp':'',
    'CityIPExp':'',
    'StreetIPExp':'',
    'HouseIPExp':'',
    'BuildIPExp':'',
    'BuildingIPExp':'',
    'FlatIPExp':'',
    'PhoneIPExp':'',


}
FirstNameArch_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_FirstNameArch',
'service': 'FirstNameArch_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
    # Блок Адрес Временный
    # 'RegionExpTmp':'45',
    # 'CityExpTmp':('МОСКВА').encode('utf8'),
    # 'StreetExpTmp':('ПОЖАРСКИЙ').encode('utf8'),
    # 'HouseExpTmp':'15',
    # 'BuildExpTmp':'',
    # 'BuildingExpTmp':'',
    # 'FlatExpTmp':'6',
    # НЕОБЯЗАТЕЛЬНЫЙ блок Поиск архивных данных
    'ExpArch':'1',
    'SurNameArch':'',
    'FirstNameArch':'!#@!#',
    'MiddleNameArch':'',
    'SeriaArch':'',
    'NumberArch':'',
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
    # 'IPExp':'1',
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


}
Flat_IPEmployer = {
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '2',
    'Employer': '1',
'ERR': 'ERROR_VALIDATION_Flat',
'service': 'Flat_IPEmployer',

    # 'OGRNIP': '312751502300034',
    'INNIP': '231293645637',
    'FIO': 'ИП Коровников Алексей Валерьевич',
    'Region': '03',
    'City': 'Выселки',
    'Street': '',
    'House': '',
    'Flat': '!#!#@',
    'Phone': '9034548390',
    'zapros': 'IP-Employer'

}
FlatExp_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_FlatExp',
'service': 'FlatExp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '!@^@#$^',
    'PhoneExp': '',
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
    # 'IPExp':'1',
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
}
FlatExpTmp_ExpFL = {
    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_FlatExpTmp',
'service': 'FlatExpTmp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    # 'RegionExp': '45',
    # 'CityExp': u'МОСКВА',
    # 'StreetExp': u'Новгородская',
    # 'HouseExp': '33',
    # 'BuildExp': '',  # или
    # 'BuildingExp': '',
    # 'FlatExp': '30',
    # 'PhoneExp': '',
    # Блок Адрес Временный
    'RegionExpTmp':'45',
    'CityExpTmp':('МОСКВА').encode('utf8'),
    'StreetExpTmp':('ПОЖАРСКИЙ').encode('utf8'),
    'HouseExpTmp':'15',
    'BuildExpTmp':'',
    'BuildingExpTmp':'',
    'FlatExpTmp':'!@#!#',
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
    # 'IPExp':'1',
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


}
FlatIPExp_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_FlatIPExp',
'service': 'FlatIPExp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
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
    'IPExp':'1',
    'OGRNIPExp':'',
    'INNIPExp': '772071873841',
    'FIOIPExp':'',
    'RegionIPExp':'',
    'CityIPExp':'',
    'StreetIPExp':'',
    'HouseIPExp':'',
    'BuildIPExp':'',
    'BuildingIPExp':'',
    'FlatIPExp':'!@#!#!',
    'PhoneIPExp':'',

}
FlatOrgExp_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_FlatOrgExp',
'service': 'FlatOrgExp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
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
    'OrgExp': '1',
    'OGRNOrgExp': '1154205015832',  # INNOrgExp
    'NameOrgExp': 'ВЕСТА',
    'RegionOrgExp': '32',
    'CityOrgExp': 'КЕМЕРОВО',
    'StreetOrgExp': 'ЛЕНИНА',  # или
    'HouseOrgExp': '128',
    'BuildOrgExp': '',
    'BuildingOrgExp': '',
    'FlatOrgExp': '!@!#@@#',
    'PhoneOrgExp': '',
    # Роботодатель ИП
    # 'IPExp':'1',
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

}
GosNumber_TS = {
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '6',
    'TS': '1',
'ERR': 'ERROR_VALIDATION_GosNumber',
'service': 'GosNumber_TS',

    'GosNumber': '!@!#',
    # 'VIN': '',

}
House_IPEmployer = {
'Type': 'Request',
              'WorkingDirectory': WD,
              'Event': '2',
              'Employer': '1',
'ERR': 'ERROR_VALIDATION_House',
'service': 'House_IPEmployer',

              #'OGRNIP': '312751502300034',
              'INNIP': '231293645637',
              'FIO': 'ИП Коровников Алексей Валерьевич',
              'Region': '03',
              'City': 'Выселки',
              'Street': '',
              'House': '!@#@$$',
              'Flat': '',
              'Phone': '9034548390',
}
HouseExp_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_HouseExp',
'service': 'HouseExp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '!#@@!!#',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
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
    # 'IPExp':'1',
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

}
HouseExpTmp_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_HouseExpTmp',
'service': 'HouseExpTmp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    # 'RegionExp': '45',
    # 'CityExp': u'МОСКВА',
    # 'StreetExp': u'Новгородская',
    # 'HouseExp': '33',
    # 'BuildExp': '',  # или
    # 'BuildingExp': '',
    # 'FlatExp': '30',
    # 'PhoneExp': '',
    # Блок Адрес Временный
    'RegionExpTmp':'45',
    'CityExpTmp':('МОСКВА').encode('utf8'),
    'StreetExpTmp':('ПОЖАРСКИЙ').encode('utf8'),
    'HouseExpTmp':'!@#!#!',
    'BuildExpTmp':'',
    'BuildingExpTmp':'',
    'FlatExpTmp':'6',
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
    # 'IPExp':'1',
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
}
HouseIPExp_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_HouseIPExp',
'service': 'HouseIPExp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
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
    'IPExp':'1',
    'OGRNIPExp':'',
    'INNIPExp': '772071873841',
    'FIOIPExp':'',
    'RegionIPExp':'',
    'CityIPExp':'',
    'StreetIPExp':'',
    'HouseIPExp':'!#!#!#@#',
    'BuildIPExp':'',
    'BuildingIPExp':'',
    'FlatIPExp':'',
    'PhoneIPExp':'',
}
HouseOrgExp_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_HouseOrgExp',
'service': 'HouseOrgExp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
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
    'OrgExp': '1',
    'OGRNOrgExp': '1154205015832',  # INNOrgExp
    'NameOrgExp': 'ВЕСТА',
    'RegionOrgExp': '32',
    'CityOrgExp': 'КЕМЕРОВО',
    'StreetOrgExp': 'ЛЕНИНА',  # или
    'HouseOrgExp': '!@!#',
    'BuildOrgExp': '',
    'BuildingOrgExp': '',
    'FlatOrgExp': '709',
    'PhoneOrgExp': '',
    # Роботодатель ИП
    # 'IPExp':'1',
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
}
InfoType_FLSVI = {
'Type': 'Request',
         'WorkingDirectory': WD,
         'Event': '3',
         'SVI': '1',
'ERR': 'ERROR_VALIDATION_InfoType',
'service': 'InfoType_FLSVI',

         'SurName': 'ХРОМОВ',
         'FirstName': 'АЛЕКСАНДР',
         'MiddleName': 'ВАЛЕРИАНОВИЧ',
         'DateOfBirth': '03.08.1969',
         'Seria': '4597',
         'Number': '005229',
         'InfoType': '#!@!#',
}
INN_ULFNSA = {
'Type': 'Request',
          'WorkingDirectory': WD,
          'Event': '1',
          'FNSA': '1',
'ERR': 'ERROR_VALIDATION_INN',
'service': 'INN_ULFNSA',

          'INN': '6002019166570',
}
INNExp_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_INNEXP',
'service': 'INNExp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    'INNExp': '77040431900456',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
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
    # 'IPExp':'1',
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

}
INNIP_IPEmployer = {
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '2',
    'Employer': '1',
'ERR': 'ERROR_VALIDATION_INNIP',
'service': 'INNIP_IPEmployer',

    # 'OGRNIP': '312751502300034',
    'INNIP': '231293645637sdv',
    'FIO': 'ИП Коровников Алексей Валерьевич',
    'Region': '03',
    'City': 'Выселки',
    'Street': '',
    'House': '',
    'Flat': '',
    'Phone': '9034548390',

}
INNIPExp_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_INNIPEXP',
'service': 'INNIPExp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
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
    'IPExp':'1',
    'OGRNIPExp':'',
    'INNIPExp': '772071873841asd',
    'FIOIPExp':'',
    'RegionIPExp':'',
    'CityIPExp':'',
    'StreetIPExp':'',
    'HouseIPExp':'',
    'BuildIPExp':'',
    'BuildingIPExp':'',
    'FlatIPExp':'',
    'PhoneIPExp':'',

}
INNOrgExp_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_INNORGEXP',
'service': 'INNOrgExp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
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
    'OrgExp': '1',
    'INNOrgExp': '1154205015832dv',  # INNOrgExp
    'NameOrgExp': 'ВЕСТА',
    'RegionOrgExp': '32',
    'CityOrgExp': 'КЕМЕРОВО',
    'StreetOrgExp': 'ЛЕНИНА',  # или
    'HouseOrgExp': '128',
    'BuildOrgExp': '',
    'BuildingOrgExp': '',
    'FlatOrgExp': '709',
    'PhoneOrgExp': '',
    # Роботодатель ИП
    # 'IPExp':'1',
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
}
IssueDate_FLCKKI = {
'Type': 'Request',
          'WorkingDirectory': WD,
          'Event': '3',
          'CKKI': '1',
'ERR': 'ERROR_VALIDATION_IssueDate',
'service': 'IssueDate_FLCKKI',

          'SurName': 'ХРОМОВ',
          'FirstName': 'АЛЕКСАНДР',
          'MiddleName': 'ВАЛЕРИАНОВИЧ',
          'DateOfBirth': '03.08.1969',
          'Seria': '4597',
          'Number': '005229',
          'IssueDate': '!#@!@!#',
}
MiddleNameArch_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_MiddleNameArch',
'service': 'MiddleNameArch_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
    # Блок Адрес Временный
    # 'RegionExpTmp':'45',
    # 'CityExpTmp':('МОСКВА').encode('utf8'),
    # 'StreetExpTmp':('ПОЖАРСКИЙ').encode('utf8'),
    # 'HouseExpTmp':'15',
    # 'BuildExpTmp':'',
    # 'BuildingExpTmp':'',
    # 'FlatExpTmp':'6',
    # НЕОБЯЗАТЕЛЬНЫЙ блок Поиск архивных данных
    'ExpArch':'1',
    'SurNameArch':'',
    'FirstNameArch':'',
    'MiddleNameArch':'!#@!#',
    'SeriaArch':'',
    'NumberArch':'',
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
    # 'IPExp':'1',
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
}
NameOrg_ULEmployer = {
'Type': 'Request',
              'WorkingDirectory': WD,
              'Event': '1',
              'Employer': '1',
'ERR': 'ERROR_VALIDATION_NameOrg',
'service': 'NameOrg_ULEmployer',

              'OGRN': '1137847271924',
              'NameOrg': chr(23),
              'Region': '40',
              'City': 'Санкт-Петербург',
              'Phone': '8129837762',
}
NameOrgExp_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_NameOrgExp',
'service': 'NameOrgExp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
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
    'OrgExp': '1',
    'OGRNOrgExp': '1154205015832',  # INNOrgExp
    'NameOrgExp': chr(23),
    'RegionOrgExp': '32',
    'CityOrgExp': 'КЕМЕРОВО',
    'StreetOrgExp': 'ЛЕНИНА',  # или
    'HouseOrgExp': '128',
    'BuildOrgExp': '',
    'BuildingOrgExp': '',
    'FlatOrgExp': '709',
    'PhoneOrgExp': '',
    # Роботодатель ИП
    # 'IPExp':'1',
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

}
Number_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_Number',
'service': 'Number_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089!#@#',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
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
    # 'IPExp':'1',
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
}
NumberArch_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_NumberArch',
'service': 'NumberArch_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
    # Блок Адрес Временный
    # 'RegionExpTmp':'45',
    # 'CityExpTmp':('МОСКВА').encode('utf8'),
    # 'StreetExpTmp':('ПОЖАРСКИЙ').encode('utf8'),
    # 'HouseExpTmp':'15',
    # 'BuildExpTmp':'',
    # 'BuildingExpTmp':'',
    # 'FlatExpTmp':'6',
    # НЕОБЯЗАТЕЛЬНЫЙ блок Поиск архивных данных
    'ExpArch':'1',
    'SurNameArch':'',
    'FirstNameArch':'',
    'MiddleNameArch':'',
    'SeriaArch':'1213',
    'NumberArch':'!#!#@',
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
    # 'IPExp':'1',
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

}
OGRN_ULEmployer = {
'Type': 'Request',
              'WorkingDirectory': WD,
              'Event': '1',
              'Employer': '1',
'ERR': 'ERROR_VALIDATION_OGRN',
'service': 'OGRN_ULEmployer',

              'OGRN': '1137847271924!#!',
              'NameOrg': 'ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ "ДЕТЕЛЬ"',
              'Region': '40',
              'City': 'Санкт-Петербург',
              'Phone': '8129837762',
}
OGRNIP_IPEmployer = {
'Type': 'Request',
              'WorkingDirectory': WD,
              'Event': '2',
              'Employer': '1',
'ERR': 'ERROR_VALIDATION_OGRNIP',
'service': 'OGRNIP_IPEmployer',

              'OGRNIP': '312751502300034!@#!@',
              # 'INNIP': '231293645637',
              'FIO': 'ИП Коровников Алексей Валерьевич',
              'Region': '03',
              'City': 'Выселки',
              'Street': '',
              'House': '',
              'Flat': '',
              'Phone': '9034548390',
}
OGRNIPExp_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_OGRNIPEXP',
'service': 'OGRNIPExp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
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
    'IPExp':'1',
    'OGRNIPExp':'!##!@',
    #'INNIPExp': '772071873841',
    'FIOIPExp':'',
    'RegionIPExp':'',
    'CityIPExp':'',
    'StreetIPExp':'',
    'HouseIPExp':'',
    'BuildIPExp':'',
    'BuildingIPExp':'',
    'FlatIPExp':'',
    'PhoneIPExp':'',


}
OGRNOrgExp_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_OGRNORGEXP',
'service': 'OGRNOrgExp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
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
    'OrgExp': '1',
    'OGRNOrgExp': '1154205015832!@#!@',  # INNOrgExp
    'NameOrgExp': 'ВЕСТА',
    'RegionOrgExp': '32',
    'CityOrgExp': 'КЕМЕРОВО',
    'StreetOrgExp': 'ЛЕНИНА',  # или
    'HouseOrgExp': '128',
    'BuildOrgExp': '',
    'BuildingOrgExp': '',
    'FlatOrgExp': '709',
    'PhoneOrgExp': '',
    # Роботодатель ИП
    # 'IPExp':'1',
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
}
Phone_IDFL = {
'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '8',
    'IDFL': '1',
'ERR': 'ERROR_VALIDATION_Phone',
'service': 'Phone_IDFL',

    'SurName': 'ПОНАМАРЕВА',
    'FirstName': 'ИРИНА',
    'MiddleName': 'ЮРЬЕВНА',
    # 'DateOfBirth': '11.01.1966',
    # 'Seria': '4004',
    # 'Number': '946593',
    #   'Address': '40 САНКТ ПЕТЕРБУРГ ВОЗНЕСЕНСКИЙ 34 1',
    'Phone': '8123106658!#!@',
    # 'GosNumber': '',
    #'INNIP': '782619098267',
    # 'OGRN': '1056900010375',
    # 'OGRNIP': '',
    # "RegionExp": '40',
    # "CityExp": 'САНКТ ПЕТЕРБУРГ',
    # "StreetExp": 'ВОЗНЕСЕНСКИЙ',
    # "HouseExp": '34',
    # "BuildExp": '1',
    # "FlatExp": '',
}
Phone_ULEmployer = {
'Type': 'Request',
              'WorkingDirectory': WD,
              'Event': '1',
              'Employer': '1',
'ERR': 'ERROR_VALIDATION_Phone',
'service': 'Phone_ULEmployer',

              'OGRN': '1137847271924',
              'NameOrg': 'ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ "ДЕТЕЛЬ"',
              'Region': '40',
              'City': 'Санкт-Петербург',
              'Phone': '8129837762!#!@#!',
}
Phone_IPEmployer = {
'Type': 'Request',
              'WorkingDirectory': WD,
              'Event': '2',
              'Employer': '1',
'ERR': 'ERROR_VALIDATION_Phone',
'service': 'Phone_IPEmployer',

              #'OGRNIP': '312751502300034',
              'INNIP': '231293645637',
              'FIO': 'ИП Коровников Алексей Валерьевич',
              'Region': '03',
              'City': 'Выселки',
              'Street': '',
              'House': '',
              'Flat': '',
              'Phone': '9034548390!#@!#!!@',
}
PhoneExp_ExpFL = {
    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_PhoneExp',
'service': 'PhoneExp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '!#!@!#',
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
    # 'IPExp':'1',
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


}
PhoneIPExp_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_PhoneIPExp',
'service': 'PhoneIPExp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
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
    'IPExp':'1',
    'OGRNIPExp':'',
    'INNIPExp': '772071873841',
    'FIOIPExp':'',
    'RegionIPExp':'',
    'CityIPExp':'',
    'StreetIPExp':'',
    'HouseIPExp':'',
    'BuildIPExp':'',
    'BuildingIPExp':'',
    'FlatIPExp':'',
    'PhoneIPExp':'!#!#!$#',



}
PhoneOrgExp_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_PhoneOrgExp',
'service': 'PhoneOrgExp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
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
    'OrgExp': '1',
    'OGRNOrgExp': '1154205015832',  # INNOrgExp
    'NameOrgExp': 'ВЕСТА',
    'RegionOrgExp': '32',
    'CityOrgExp': 'КЕМЕРОВО',
    'StreetOrgExp': 'ЛЕНИНА',  # или
    'HouseOrgExp': '128',
    'BuildOrgExp': '',
    'BuildingOrgExp': '',
    'FlatOrgExp': '709',
    'PhoneOrgExp': '!#@!@#',
    # Роботодатель ИП
    # 'IPExp':'1',
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


}
PlaceOfBirth_FLFR = {
'Type': 'Request',
            'WorkingDirectory' : WD,
            'Event': '3',
            'FR': '1',
'ERR': 'ERROR_VALIDATION_PlaceOfBirth',
'service': 'PlaceOfBirth_FLFR',

            'SurName' : 'ХРОМОВ',
            'FirstName' : 'АЛЕКСАНДР',
            'MiddleName' : 'ВАЛЕРИАНОВИЧ',
            'DateOfBirth': '03.08.1969',
            'Seria': '3213',
            'Number': '321321',
    'PlaceOfBirth': '!@#!#!@'
}
Region_ULEmployer = {
'Type': 'Request',
              'WorkingDirectory': WD,
              'Event': '1',
              'Employer': '1',
'ERR': 'ERROR_VALIDATION_Region',
'service': 'Region_ULEmployer',

              'OGRN': '1137847271924',
              'NameOrg': 'ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ "ДЕТЕЛЬ"',
              'Region': '!@!#',
              'City': 'Санкт-Петербург',
              'Phone': '8129837762',
}
RegionExp_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_RegionExp',
'service': 'RegionExp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '!@!@',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
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
    # 'IPExp':'1',
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

}
RegionExpTmp_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_RegionExpTmp',
'service': 'RegionExpTmp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    # 'RegionExp': '45',
    # 'CityExp': u'МОСКВА',
    # 'StreetExp': u'Новгородская',
    # 'HouseExp': '33',
    # 'BuildExp': '',  # или
    # 'BuildingExp': '',
    # 'FlatExp': '30',
    # 'PhoneExp': '',
    # Блок Адрес Временный
    'RegionExpTmp':'!#@!@',
    'CityExpTmp':('МОСКВА').encode('utf8'),
    'StreetExpTmp':('ПОЖАРСКИЙ').encode('utf8'),
    'HouseExpTmp':'15',
    'BuildExpTmp':'',
    'BuildingExpTmp':'',
    'FlatExpTmp':'6',
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
    # 'IPExp':'1',
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

}
RegionIPExp_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_RegionIPExp',
'service': 'RegionIPExp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
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
    'IPExp':'1',
    'OGRNIPExp':'',
    'INNIPExp': '772071873841',
    'FIOIPExp':'',
    'RegionIPExp':'!#!#',
    'CityIPExp':'',
    'StreetIPExp':'',
    'HouseIPExp':'',
    'BuildIPExp':'',
    'BuildingIPExp':'',
    'FlatIPExp':'',
    'PhoneIPExp':'',

}
RegionOrgExp_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_RegionOrgExp',
'service': 'RegionOrgExp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
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
    'OrgExp': '1',
    'OGRNOrgExp': '1154205015832',  # INNOrgExp
    'NameOrgExp': 'ВЕСТА',
    'RegionOrgExp': '!@#',
    'CityOrgExp': 'КЕМЕРОВО',
    'StreetOrgExp': 'ЛЕНИНА',  # или
    'HouseOrgExp': '128',
    'BuildOrgExp': '',
    'BuildingOrgExp': '',
    'FlatOrgExp': '709',
    'PhoneOrgExp': '',
    # Роботодатель ИП
    # 'IPExp':'1',
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

}
Seria_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_Seria',
'service': 'Seria_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500!@',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
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
    # 'IPExp':'1',
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

}
Seria_BSIP = {
'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '7',
    'BIP': '1',
'ERR': 'ERROR_VALIDATION_Seria',
'service': 'Seria_BSIP',

    'SurName': 'ХРОМОВ',
    'FirstName': 'АЛЕКСАНДР',
    'MiddleName': 'ВАЛЕРИАНОВИЧ',
    'DateOfBirth': '03.08.1969',
    'Seria': '4597!##@',
    'Number': '00522',
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
}
Seria_UPassporta = {
'Type': 'Request',
                   'WorkingDirectory': WD,
                   'Event': '4',
                   'UPassporta': '1',
'ERR': 'ERROR_VALIDATION_Seria',
'service': 'Seria_UPassporta',

                   'Seria': '4500@#!@',
                   'Number': '375473',
                   'zapros': 'Pasp-UPassporta'
}
SeriaArch_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_SeriaArch',
'service': 'SeriaArch_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
    # Блок Адрес Временный
    # 'RegionExpTmp':'45',
    # 'CityExpTmp':('МОСКВА').encode('utf8'),
    # 'StreetExpTmp':('ПОЖАРСКИЙ').encode('utf8'),
    # 'HouseExpTmp':'15',
    # 'BuildExpTmp':'',
    # 'BuildingExpTmp':'',
    # 'FlatExpTmp':'6',
    # НЕОБЯЗАТЕЛЬНЫЙ блок Поиск архивных данных
    'ExpArch':'1',
    'SurNameArch':'',
    'FirstNameArch':'',
    'MiddleNameArch':'',
    'SeriaArch':'!#@!',
    'NumberArch':'123213',
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
    # 'IPExp':'1',
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

}
Street_IPEmployer = {'Type': 'Request',
              'WorkingDirectory': WD,
              'Event': '2',
              'Employer': '1',
'ERR': 'ERROR_VALIDATION_Street',
'service': 'Street_IPEmployer',

              #'OGRNIP': '312751502300034',
              'INNIP': '231293645637',
              'FIO': 'ИП Коровников Алексей Валерьевич',
              'Region': '03',
              'City': 'Выселки',
              'Street': '!@!#!',
              'House': '',
              'Flat': '',
              'Phone': '9034548390',}
StreetExp_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_StreetExp',
'service': 'StreetExp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'!#!$@$!$',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
    # Блок Адрес Временный
    # 'RegionExpTmp':'45',
    # 'CityExpTmp':('МОСКВА').encode('utf8'),
    # 'StreetExpTmp':('ПОЖАРСКИЙ').encode('utf8'),
    # 'HouseExpTmp':'15',
    # 'BuildExpTmp':'',
    # 'BuildingExpTmp':'',
    # 'FlatExpTmp':'6',
    # НЕОБЯЗАТЕЛЬНЫЙ блок Поиск архивных данных
    # 'ExpArch':'1',
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
    # 'IPExp':'1',
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

}
StreetExpTmp_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_StreetExpTmp',
'service': 'StreetExpTmp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    # 'RegionExp': '45',
    # 'CityExp': u'МОСКВА',
    # 'StreetExp': u'Новгородская',
    # 'HouseExp': '33',
    # 'BuildExp': '',  # или
    # 'BuildingExp': '',
    # 'FlatExp': '30',
    # 'PhoneExp': '',
    # Блок Адрес Временный
    'RegionExpTmp':'45',
    'CityExpTmp':('МОСКВА').encode('utf8'),
    'StreetExpTmp':'@#$!$@$',
    'HouseExpTmp':'15',
    'BuildExpTmp':'',
    'BuildingExpTmp':'',
    'FlatExpTmp':'6',
    # НЕОБЯЗАТЕЛЬНЫЙ блок Поиск архивных данных
    # 'ExpArch':'1',
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
    # 'IPExp':'1',
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

}
StreetIPExp_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_StreetIPExp',
'service': 'StreetIPExp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
    # Блок Адрес Временный
    # 'RegionExpTmp':'45',
    # 'CityExpTmp':('МОСКВА').encode('utf8'),
    # 'StreetExpTmp':('ПОЖАРСКИЙ').encode('utf8'),
    # 'HouseExpTmp':'15',
    # 'BuildExpTmp':'',
    # 'BuildingExpTmp':'',
    # 'FlatExpTmp':'6',
    # НЕОБЯЗАТЕЛЬНЫЙ блок Поиск архивных данных
    # 'ExpArch':'1',
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
    'IPExp':'1',
    'OGRNIPExp':'',
    'INNIPExp': '772071873841',
    'FIOIPExp':'',
    'RegionIPExp':'',
    'CityIPExp':'',
    'StreetIPExp':'@#$!$@',
    'HouseIPExp':'',
    'BuildIPExp':'',
    'BuildingIPExp':'',
    'FlatIPExp':'',
    'PhoneIPExp':'',

}
StreetOrgExp_ExpFL = {

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_StreetOrgExp',
'service': 'StreetOrgExp_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
    # Блок Адрес Временный
    # 'RegionExpTmp':'45',
    # 'CityExpTmp':('МОСКВА').encode('utf8'),
    # 'StreetExpTmp':('ПОЖАРСКИЙ').encode('utf8'),
    # 'HouseExpTmp':'15',
    # 'BuildExpTmp':'',
    # 'BuildingExpTmp':'',
    # 'FlatExpTmp':'6',
    # НЕОБЯЗАТЕЛЬНЫЙ блок Поиск архивных данных
    # 'ExpArch':'1',
    # 'SurNameArch':'',
    # 'FirstNameArch':'',
    # 'MiddleNameArch':'',
    # 'SeriaArch':'',
    # 'NumberArch':'',
    # НЕОБЯЗАТЕЛЬНЫЙ блок Проверка работодателя
    # Роботодатель ЮЛ
    'OrgExp': '1',
    'OGRNOrgExp': '1154205015832',  # INNOrgExp
    'NameOrgExp': 'ВЕСТА',
    'RegionOrgExp': '32',
    'CityOrgExp': 'КЕМЕРОВО',
    'StreetOrgExp': '@$!!@$@',  # или
    'HouseOrgExp': '128',
    'BuildOrgExp': '',
    'BuildingOrgExp': '',
    'FlatOrgExp': '709',
    'PhoneOrgExp': '',
    # Роботодатель ИП
    # 'IPExp':'1',
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

}
SurNameArch_ExpFL ={

    # Основной блок
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '3',
    'Exp': '1',
'ERR': 'ERROR_VALIDATION_SurNameArch',
'service': 'SurNameArch_ExpFL',

    'SurName': u'Пушкин',
    'FirstName': u'Александр',
    'MiddleName': '',
    'DateOfBirth': '06.03.1966',
    'Seria': '4500',
    'Number': '362089',
    # 'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'Новгородская',
    'HouseExp': '33',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '30',
    'PhoneExp': '',
    # Блок Адрес Временный
    # 'RegionExpTmp':'45',
    # 'CityExpTmp':('МОСКВА').encode('utf8'),
    # 'StreetExpTmp':('ПОЖАРСКИЙ').encode('utf8'),
    # 'HouseExpTmp':'15',
    # 'BuildExpTmp':'',
    # 'BuildingExpTmp':'',
    # 'FlatExpTmp':'6',
    # НЕОБЯЗАТЕЛЬНЫЙ блок Поиск архивных данных
    'ExpArch':'1',
    'SurNameArch':'$@!$@$',
    'FirstNameArch':'',
    'MiddleNameArch':'',
    'SeriaArch':'',
    'NumberArch':'',
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
    # 'IPExp':'1',
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

}
VIN_TS = {
'Type': 'Request',
            'WorkingDirectory': WD,
            'Event': '6',
            'TS': '1',
'ERR': 'ERROR_VALIDATION_VIN',
'service': 'VIN_TS',

            # 'GosNumber': 'M775XY27',
            'VIN': '@$!$',
}


FL = [
Address_IDFL,
BuildExp_ExpFL,
BuildOrgExp_ExpFL,
CityExp_ExpFL,
CityExpTmp_ExpFL,
CityIPExp_ExpFL,
CityOrgExp_ExpFL,
DateOfBirth_ExpFL,
SURNAME_ExpFL,
FIRSTNAME_ExpFL,
MIDDLENAME_ExpFL,
FIOIPExp_ExpFL,
FirstNameArch_ExpFL,
FlatExp_ExpFL,
FlatExpTmp_ExpFL,
FlatIPExp_ExpFL,
FlatOrgExp_ExpFL,
HouseExp_ExpFL,
HouseExpTmp_ExpFL,
HouseIPExp_ExpFL,
HouseOrgExp_ExpFL,
InfoType_FLSVI,
INNExp_ExpFL,
INNIPExp_ExpFL,
INNOrgExp_ExpFL,
IssueDate_FLCKKI,
MiddleNameArch_ExpFL,
NameOrgExp_ExpFL,
Number_ExpFL,
NumberArch_ExpFL,
OGRNIPExp_ExpFL,
OGRNOrgExp_ExpFL,
Phone_IDFL,
PhoneExp_ExpFL,
PhoneIPExp_ExpFL,
PhoneOrgExp_ExpFL,
PlaceOfBirth_FLFR,
RegionExp_ExpFL,
RegionExpTmp_ExpFL,
RegionIPExp_ExpFL,
RegionOrgExp_ExpFL,
Seria_ExpFL,
SeriaArch_ExpFL,
StreetExp_ExpFL,
StreetExpTmp_ExpFL,
StreetIPExp_ExpFL,
StreetOrgExp_ExpFL,
SurNameArch_ExpFL,
      ]
UL = [
City_ULEmployer,
INN_ULFNSA,
NameOrg_ULEmployer,
OGRN_ULEmployer,
Phone_ULEmployer,
Region_ULEmployer,
    ]
IP =[
FIO_IPEmployer,
Flat_IPEmployer,
House_IPEmployer,
INNIP_IPEmployer,
OGRNIP_IPEmployer,
Phone_IPEmployer,
Seria_BSIP,
Street_IPEmployer,
]
PASP = [
    Seria_UPassporta,
]
BSUL = []
BSIP = []
ID_FL = []
BS_R = []
GIBDD = [
GosNumber_TS,
VIN_TS
]

Services = [UL,
            IP,
            FL,
            PASP,
            BSUL,
            GIBDD,
            BSIP,
            ID_FL,
            BS_R]

def login():
    post={
                    'Type': 'Login',
                    'Login': LOGIN,
                    'Password': PASSWORD}
    r = R.post(URL,data=post, headers=HEADERS,  verify=False) #'C:\Soft\Тестирование\КриптоПро\ssl.croinform.ru.cer'
    lx = html.fromstring(r.content)
    WD = lx.xpath('//text()')[1]
    print('WD ' + str(WD))
    return WD

def request(WD,service):
    service['WorkingDirectory'] = WD
    r = requests.post(URL,data=service,headers=HEADERS, verify=False,timeout=200)
    lx = html.fromstring(r.content)
    RN = lx.xpath('//text()')[1]
    if RN == (service['ERR']).upper():
        pass
        print(service['ERR'] + ' : ' + service['service'] + ' : OK')
    else:
        print(service['ERR'] + ' : ' + service['service'] + ' : notOK')
        ERRORS.append(service['ERR'] + ' : ' + RN + ' : ' + service['service'])

        # print(service['ERR'] + ' : ' + str(service['ERR'])[17:] + ' - ' + str(service[str((service['ERR'])[17:])]))
        # DATA.append(service['ERR'] + ' : ' + str(service['ERR'])[17:] + ' - ' + str(service[str((service['ERR'])[17:])]))

def logout(WD):
    post={
                            'Type': 'Logout',
                            'WorkingDirectory': WD,
                        }
    r = requests.post(URL, data=post, headers=HEADERS,verify=False,)
    print(r.status_code)





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
        #     for key, value in RNs.items():
        #             resp = response(WD, key, value)
        #             while resp == 'err':
        #                 WD = login()
        #                 sleep(3)
        #                 if WD != 'ERROR_VALIDATION_WORKINGDIRECTORY':
        #                     resp = response(WD, key, value)
        #                     break
        #
        #
        #     it+=1



        # ЕДИНИЧНЫЙ ЗАПРОС

        service = CityIPExp_ExpFL
        RN = request(WD, service)




        # НАГРУЗКА

        # service = FLExp
        # t = 0
        # while t < 20:
        #     RN = request(WD, service)
        #     #response(WD, RN, service)
        #     sleep(1)
        #     t += 1


        logout(WD)

        print(Exceptions)
        print('ERRORS:')
        for i in ERRORS:
            print(i)

        print('****************************************************')
        for i in DATA:
            print(i)

    except Exception as e:
        print(e)


