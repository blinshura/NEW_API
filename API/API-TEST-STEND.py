from lxml import etree
from time import sleep
import requests
from bs4 import BeautifulSoup
from lxml import html
import re

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


URL = 'http://vips2:3777/api.test' #'http://ips1:3777/test'  #ips1: 192.168.0.118:450  vips1: 192.168.0.135:3777
LOGIN = 'testAutomatUser' #'Svetka' #'ander_автомат'
PASSWORD = 'testAutomatUser'#'testAutomatUser' #'153759' #'687dd78R'
Exceptions = []
ERRORS = []
HEADERS={
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'}
WD = ''
RNs = {}


# сервисы


UL = {'Type': 'Request',
          'WorkingDirectory': WD,
          'Event': '1',
          'FNST': '1',
          'OGRN': '1177746172790',
          #'INN': '3213213211',
          'zapros': 'UL-FNST'}  # 0

IP = {'Type': 'Request',
         'WorkingDirectory': WD,
         'Event': '2',
         'IPT': '1',
         'OGRNIP' : '312751502300034',
         'zapros': 'IP'}  # 0

FL = {'Type': 'Request',
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

PASP = {'Type': 'Request',
                   'WorkingDirectory': WD,
                   'Event': '4',
                   'UPassporta': '1',
                   'Seria': '4852',
                   'Number': '480529',
                   'zapros': 'Pasp'}  # 0

BSUL = {'Type': 'Request',
           'WorkingDirectory': WD,
           'Event': '1',
           'BS': '1',
           'OGRN': '1177746172790',
           'zapros': 'BSUL-BS'}  # 0

TS = {'Type': 'Request',
            'WorkingDirectory': WD,
            'Event': '6',
            'TS': '1',
            'GosNumber': 'М982ММ99',
            # 'VIN': '',
            'zapros': 'TS'
            }  # 0

BSIP = {
    'Type': 'Request',
    'WorkingDirectory': WD,
    'Event': '7',
    'BIP': '1',
    'SurName': 'ХРОМОВ',
    'FirstName': 'АЛЕКСАНДР',
    'MiddleName': 'ВАЛЕРИАНОВИЧ',
    'DateOfBirth': '03.08.1969',
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



Services = [UL,
            IP,
            FL,
            PASP,
            BSUL,
            TS,
            BSIP,
            IDFL,
            ]

def login():
    post={
                    'Type': 'Login',
                    'Login': LOGIN,
                    'Password': PASSWORD}
    r = requests.post(URL,data=post,headers=HEADERS, verify=False,)
    # print(r.text)
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
    r = True #rg.search(RN)
    if r:
        print('RN ' + str(RN))
        print(service['zapros'] + ' - ' + 'RN: ' + str(RN) + '\n')
    else:
        print(RN)
        print(service['zapros'] + ' - ' + 'ERROR: ' + RN + '\n')
        ERRORS.append(service['zapros'] + ' - ' + 'ERROR: ' + RN)
        #ERRORS.append(RN)
        ERRORS.append('---------------------------')
    RNs[RN]= service
    return RN

def response(WD, RN, service):
    StatusANS = '3'
    tryes = 30
    while StatusANS == '3' and tryes >= 1:

        post = {'Type': 'Answer',
                'WorkingDirectory': WD,
                'RequestNumber': RN,
                'TypeAnswer': 'HV',
                }
        post['RequestNumber'] = RN
        post['WorkingDirectory'] = WD
        r = requests.post(URL, data=post, headers=HEADERS, verify=False,)
        print(r.text)

        ANSWER = BeautifulSoup(r.content, 'lxml')

        if ANSWER.find('statusrequest') !=None:
            StatusANS = ANSWER.statusrequest.text
            StatusANS = str(StatusANS)
        else:
            lx = html.fromstring(r.content)
            print(r.text)
            StatusANS = lx.xpath('//text()')[3]
            StatusANS = str(StatusANS)
            print(StatusANS)



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

            #print(service['zapros'] + ' - OK!!!!!!!')

        if StatusANS == '3': sleep(10)

        print('\n' + 'ANS-' + StatusANS + '  try-' + str(tryes) + '  ' + service['zapros'])
        tryes -= 1
        if StatusANS == '3' and tryes < 1:
            ERRORS.append(service['zapros'])
            ERRORS.append(RN + ' Не дождались ответа')
            ERRORS.append('---------------------------')
            print(' Не дождались ответа')
    print('-----------------------------------------------------------------------------------------------------------')

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

        it = 0
        while it < 1:
            for S in Services:
                RN = request(WD, S)
            print('========================================================================')

            for key, value in RNs.items():
                    response(WD, key, value)

            it+=1



        # ЕДИНИЧНЫЙ ЗАПРОС фыа

        # service = TS
        # RN = request(WD, service)
        # response(WD, RN, service)



        # НАГРУЗКА

        # service = ULAFF
        # t = 0
        # while t < 100:
        #     RN = request(WD, service)
        #     response(WD, RN, service)
        #     t += 1


        logout(WD)

        print(Exceptions)
        print('ERRORS:')
        for i in ERRORS:
            print(i)

    except Exception as e:
        print(e)


