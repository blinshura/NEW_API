from time import sleep
import requests
from bs4 import BeautifulSoup
from lxml import html
import re


URL = 'http://ips3:777/api.php'  #ips1: 192.168.0.118:450  vips1: 192.168.0.135:3777
LOGIN = 'Test_61959959'
PASSWORD = '5253325'
Exceptions = []
ERRORS = []
HEADERS={
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'}
WD = ''
RNs = {}



# сервисы
ULFNST = {'Type': 'Request',
          'WorkingDirectory': WD,
          'Event': '1',
          'FNST': '1',
          'OGRN': '1177746172790',
          #'INN': '3213213211',
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
            'OGRN': '1177746172790',
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
         'OGRN': '1177746172790',
         'zapros': 'UL-AFF'}  # 6
ULEmployer = {'Type': 'Request',
              'WorkingDirectory': WD,
              'Event': '1',
              'Employer': '1',
              'OGRN': '1177746172790',
              'zapros': 'UL-Employer'}  # 7
ULExtSource = {'Type': 'Request',
               'WorkingDirectory': WD,
               'Event': '1',
               'ExtSource': '1',
               'OGRN': '1177746172790',
               'zapros': 'UL-ExtSource'}  # 8

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
                'zapros': 'IP-ExtendedIP'}  # 2
IPEmployer = {'Type': 'Request',
              'WorkingDirectory': WD,
              'Event': '2',
              'Employer': '1',
              'OGRNIP': '312751502300034',
              'FIO': '',
              'Region': '',
              'City': '',
              'Street': '',
              'House': '',
              'Flat': '',
              'Phone': '',
              'zapros': 'IP-Employer'
              }  # 3
IPExtSource = {'Type': 'Request',
               'WorkingDirectory': WD,
               'Event': '2',
               'ExtSource': '1',
               'OGRNIP': '312751502300034',
               'zapros': 'IP-ExtSource'}  # 4

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
             'MiddleName': 'ВАЛЕРИАНОВИЧ',
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
         'MiddleName': 'ВАЛЕРИАНОВИЧ',
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
    'SurName': u'хромов',
    'FirstName': u'александр',
    'MiddleName': u'валерианович',
    'DateOfBirth': '03.08.1969',
    'Seria': '4597',
    'Number': '005229',
    'INNExp': '770404319004',
    # Блок Адрес Постоянный
    'RegionExp': '45',
    'CityExp': u'МОСКВА',
    'StreetExp': u'ПОЖАРСКИЙ',
    'HouseExp': '15',
    'BuildExp': '',  # или
    'BuildingExp': '',
    'FlatExp': '6',
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
    'PhoneOrgExp': '',
    # Роботодатель ИП
    #'IPExp':'1',
    # 'OGRNIPExp':'',
    #'INNIPExp': '772071873841',
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
    'DateOfBirth': '03.08.1969',
    'Seria': '4597',
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
    'zapros': 'PSIP-BIP'
}  # 0

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
    'Number': '005220',
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
    'BSR': '1',
    'WorkingDirectory': WD,
    # -----------------------------------------------------------------------------------------------------------------------
    'NameOrg': 'ГАЛС ПРОМ',
    'OGRN': '1133703000683',
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

UL = [ULFNST,
      ULFNSA,
      # ULGIBDD,
      ULBalans,
      ULSVI,
      ULBenef,
      ULAFF,
      ULEmployer,
      ULExtSource
      ]  # 0
IP = [IPIPT,
      IPIPA,
      IPExtendedIP,
      IPEmployer,
      IPExtSource
      ]  # 1
FL = [
    # FLGIBDD,
    FLCASBO,
    FLCASBR,
    FLRaiting,
    FLRaitingR,
    FLRaiting_2,
    FLRaiting_2R,
    # FLFR,
    FLAFF,
    FLCKKI,
    FLSVI,
    FLExp,
    FLExtSource,
]  # 2
PASP = [
    PASP_UPassporta,
    PASP_PPFMS,
]  # 3
BSUL = [
    BSUL_BS,
    BSUL_BSPD,
    BSUL_SVI,
]  # 4
GIBDD = [
    GIBDD_TS,
    GIBDD_BCars,
    GIBDD_SCars,
] # 5
BSIP = [
    BSIP_BIP,
]  # 6
ID_FL = [
    IDFL
]  # 7
BS_R = [
    BSUL_RASH
]  # 8

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
    post={
                    'Type': 'Login',
                    'Login': LOGIN,
                    'Password': PASSWORD}
    r = requests.post(URL,data=post,headers=HEADERS, verify=False,)
    lx = html.fromstring(r.content)
    WD = lx.xpath('//text()')[1]
    print('WD ' + str(WD))
    return WD




def request(WD,service):
    service['WorkingDirectory'] = WD
    r = requests.post(URL,data=service,headers=HEADERS, verify=False,)
    lx = html.fromstring(r.content)
    RN = lx.xpath('//text()')[1]
    re1 = "[A-Z0-9]{8}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{12}"
    rg = re.compile(re1,re.IGNORECASE|re.DOTALL)
    r = rg.search(RN)
    if r:
        print('RN ' + str(RN))
        # print(service['zapros'] + ' - ' + 'RN: ' + str(RN) + '\n')

    else:
        print(RN)
        # print(service['zapros'] + ' - ' + 'ERROR: ' + RN + '\n')
        # ERRORS.append(service['zapros'] + ' - ' + 'ERROR: ' + RN)
        # #ERRORS.append(RN)
        # ERRORS.append('---------------------------')

    RNs[RN]= service
    return RN


def response(WD, RN, service):
    ANS = '3'
    tryes = 30
    while ANS == '3' and tryes >= 1:

        post = {'Type': 'Answer',
                'WorkingDirectory': WD,
                'RequestNumber': RN,
                'TypeAnswer': 'HV'}
        post['RequestNumber'] = '9BS27112731'
        post['WorkingDirectory'] = WD
        r = requests.post(URL, data=post, headers=HEADERS, verify=False,)
        print(r.text)
        lx = html.fromstring(r.content)
        ANS = lx.xpath('//text()')[1]
        ANS = str(ANS)
        ANSWER = BeautifulSoup(r.content, 'lxml')
        #print(ANSWER)

        if ANS == '3': sleep(10)

        # Очистка ответа
        if ANS != '3':
            if '<td>' in str(ANSWER):
                for t in ANSWER.find_all('td'):
                    t = str(t).replace('<td></td>', '\n')
                    t = t.replace('</td>', '')
                    t = t.replace('<td>', '')
                    print(t)

            else:
                for t in ANSWER.find_all('div'):
                    if 'script' not in str(t):
                        t = str(t).replace('</div>', '')
                        t = t.replace('<div>', '')
                        t = t.replace('</p>', '')
                        t = t.replace('<p>', '')
                        t = t.replace('</li>', '')
                        t = t.replace('</ol>', '')
                        t = t.replace('<ol>', '')
                        t = t.replace('<li>', '')
                        t = t.replace('<span>', '')
                        t = t.replace('</span>', '')
                        print(t)



        print('\n' + 'ANS-' + ANS + '  try-' + str(tryes) + '  ' + service['zapros'])
        tryes -= 1
        if ANS == '3' and tryes < 1:
            ERRORS.append(service['zapros'])
            ERRORS.append(RN + ' Не дождались ответа')
            ERRORS.append('---------------------------')
            print(' Не дождались ответа')
    print('-----------------------------------------------------------------------------------------')

def logout(WD):
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




if __name__ == '__main__':



    try:

        WD = login()

        # ЦИКЛ ПО ВСЕМ СЕРВИСАМ

        # it = 0
        # while it < 100:
        #     for S in Services:
        #         for s in S:
        #             RN = request(WD, s)
        #
        #     for key, value in RNs.items():
        #             response(WD, key, value)
        #
        #     it+=1



        # ЕДИНИЧНЫЙ ЗАПРОС

        RN = request(WD, BSUL_RASH)
        response(WD, RN, BSUL_RASH)



        # НАГРУЗКА

        # t = 0
        # while t < 100:
        #     RN = request(WD, FLExp)
        #     response(WD, RN, FLExp)
        #     t += 1


        logout(WD)

        print(Exceptions)
        print('ERRORS:')
        for i in ERRORS:
            print(i)

    except Exception as e:
        print(e)


