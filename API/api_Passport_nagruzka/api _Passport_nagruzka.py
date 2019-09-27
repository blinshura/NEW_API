from time import sleep
import re
from lxml import html
import requests
from bs4 import BeautifulSoup
import random

URL = 'http://vips1:3777/api'  #ips1: 192.168.0.118:450  vips1: 192.168.0.135:3777
LOGIN = 'demo'#'demo' #'Svetka' #'ander_автомат'
PASSWORD = 'demo'#'Gfd!1qaz40' #'153759' #'687dd78R'
R = requests.Session()
Exceptions = []
ERRORS = []
HEADERS={
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'}
WD = ''
RNs = {}



PPFMS = {
'Type': 'Request',
              'WorkingDirectory': WD,
              'Event': '4',
              'PPFMS': '1',
              'Seria': '4500',
              'Number': '375473',
              'zapros': 'Pasp-PPFMS'
}


def login():

    post={
                    'Type': 'Login',
                    'Login': LOGIN,
                    'Password': PASSWORD}
    r = R.post(URL,data=post, headers=HEADERS,  verify=False) #'C:\Soft\Тестирование\КриптоПро\ssl.croinform.ru.cer'
    #print(r.text)
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
    rg = rg.search(RN)
    if rg:
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
        #print(r.text)


        ANSWER = BeautifulSoup(r.content, 'lxml')

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

        if StatusANS == '3': sleep(3)

        print('\n' + 'ANS-' + StatusANS + '  try-' + str(tryes) + '  ' + service['zapros'] + '  ' + RN)
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

WD = login()

with open("data", 'r', encoding='utf-8') as f:
    for i,line in enumerate(f):
        passport = line.split(';')[0]
        PPFMS['Seria'] = passport[:4]
        PPFMS['Number'] = passport[4:]
        RN = request(WD, PPFMS)
        #response(WD, RN, service)

logout(WD)