from datetime import datetime
from grab import *
from lxml import html
import threading
from time import sleep
import logging
from bs4 import BeautifulSoup, CData


logging.basicConfig(level=logging.DEBUG)


URL = 'http://192.168.0.49:777/api.php' # ips3 'http://192.168.0.23:777/api.php'
PATH = '*'
REQUEST_DATA = []
Host = "ips2:777"
WORKINGDIRECTORY = []
REQUESTNUMDER = []
VECTORS = []

def login():

    g = Grab(timeout=100, connect_timeout=30)
    g.setup(post={
        'Type': 'Login',
        'Login': 'Test_61959959',
        'Password': '5253325'
    },
        headers={
            #'Accept-Encoding': 'gzip,deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            #'Content-Length': '47',
            'Host': Host,
            #'Connection': 'Keep-Alive',


    }

    )

    go = g.go(URL)
    #print(g.xpath_text(PATH))
    xmlBODY = (go.body)
    #print(xmlBODY)
    lx = html.fromstring(xmlBODY)

    WD = lx.xpath('//text()')[1]
    print(WD)
    WORKINGDIRECTORY.append(WD)

def request(wd):


    g = Grab(timeout=100, connect_timeout=30)
    g.setup(post={
        'Type': 'Request',
        'Event': '9',
        'WorkingDirectory': wd,
#-----------------------------------------------------------------------------------------------------------------------
        'NameOrg': 'ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ "НЕОКОМПАНИ"',
        'OGRN': '1066367043038     ',
        'INN': '6367053858    ',
        'KPP': '636701001',
        'RegistrationDate': '25.03.1994',
        'authCapital': '10000',
        'OKVED': '14.12',
#-----------------------------------------------------------------------------------------------------------------------
        'addressList[0][addressType]': 'L',
        'addressList[0][Region]': '80',
        'addressList[0][City]': 'УФА',
        'addressList[0][Street]': 'МЕНДЕЛЕЕВА',
        'addressList[0][House]': '134',
        'addressList[0][Build]': '10',###
        'addressList[0][Building]': '',###
        'addressList[0][Office]': '',###

        'contactInfo[0][Phone]': '4958555668',
        'contactInfo[0][Fax]': '4959555668',###
        # Директор
        'leaderInfoList[0][LeaderCode]': 'L1',
        'leaderInfoList[0][SurName]': 'Ахметов',
        'leaderInfoList[0][FirstName]': 'Фаиль',
        'leaderInfoList[0][MiddleName]': 'Сагитович',###
        'leaderInfoList[0][DateOfBirth]': '22.01.1963',
        'leaderInfoList[0][Seria]': '8097',
        'leaderInfoList[0][Number]': '011436',
        # ФЛ Участники
        'participantInfoList[0][ParticipantCode]': 'P1',
        'participantInfoList[0][SurName]': 'Карпов',
        'participantInfoList[0][FirstName]': 'Сергей',
        'participantInfoList[0][MiddleName]': 'Владимирович',###
        'participantInfoList[0][DateOfBirth]': '24.06.1974',
        'participantInfoList[0][Seria]': '8004',
        'participantInfoList[0][Number]': '181211',
        'participantInfoList[0][AuthCapShare]': '54000',
        # ЮЛ Участники
        'legalInfoList[0][OGRN]': '1087746801130',
        'legalInfoList[0][AuthCapShare]': '16000',
#-----------------------------------------------------------------------------------------------------------------------
        'addressList[1][addressType]':'F',
        'addressList[1][Region]':'',
        'addressList[1][City]':'Москва',
        'addressList[1][Street]':'СЕМЕНОВСКАЯ Б',
        'addressList[1][House]':'40',
        'addressList[1][Build]':'',
        'addressList[1][Building]':'18',
        'addressList[1][Office]':'',

        'contactInfo[1][Phone]':'4990007878',
        'contactInfo[1][Fax]':'4990007870',

        'leaderInfoList[1][LeaderCode]':'L2',
        'leaderInfoList[1][SurName]':'ЛИЧАГИН',
        'leaderInfoList[1][FirstName]':'ПАВЕЛ',
        'leaderInfoList[1][MiddleName]':'АНАТОЛЬЕВИЧ',
        'leaderInfoList[1][DateOfBirth]':'10.10.1965',
        'leaderInfoList[1][Seria]':'4321',
        'leaderInfoList[1][Number]':'654321',

        'participantInfoList[1][ParticipantCode]':'P1',
        'participantInfoList[1][SurName]':'ЛИЧАГИН',
        'participantInfoList[1][FirstName]':'ПАВЕЛ',
        'participantInfoList[1][MiddleName]':'',
        'participantInfoList[1][DateOfBirth]':'10.10.1970',
        'participantInfoList[1][Seria]':'1234',
        'participantInfoList[1][Number]':'123456',
        'participantInfoList[1][AuthCapShare]':'1000',

        'legalInfoList[1][OGRN]':'1027700107599',
        'legalInfoList[1][AuthCapShare]':'15000'


    },
        headers={
            #'Accept-Encoding': 'gzip,deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            #'Content-Length': '1348',
            'Host': "ips2:777",
            #'Connection': 'Keep-Alive'
        }

    )


    go = g.go(URL)
    # print(g.xpath_text(PATH))
    xmlBODY = (go.body)
    lx = html.fromstring(xmlBODY)

    RN = lx.xpath('//text()')[1]
    print(RN)
    REQUESTNUMDER.append(RN)


def answer(rn,wd):

    g = Grab(timeout=100, connect_timeout=30)
    g.setup(post={
        'Type': 'Answer',
        'TypeAnswer': 'V',
        'RequestNumber': rn,
        'WorkingDirectory': wd
    },
        headers={
            # 'Accept-Encoding': 'gzip,deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Content-Length': '47',
            'Host': Host,
            # 'Connection': 'Keep-Alive',

        }

    )

    go = g.go(URL)
    # print(g.xpath_text(PATH))
    xmlBODY = (go.body)
    # print(xmlBODY)
    lx = html.fromstring(xmlBODY)
    status_request = lx.xpath('//bs_r/text()')[0]
    print(status_request)

    while status_request == '3':
        #print(xmlBODY)
        sleep(30)
        g = Grab(timeout=100, connect_timeout=30)
        g.setup(post={
            'Type': 'Answer',
            'TypeAnswer': 'V',
            'RequestNumber': rn,
            'WorkingDirectory': wd
        },
            headers={
                # 'Accept-Encoding': 'gzip,deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                # 'Content-Length': '47',
                'Host': Host,
                # 'Connection': 'Keep-Alive',

            }

        )

        go = g.go(URL)
        # print(g.xpath_text(PATH))
        xmlBODY = (go.body)
        # print(xmlBODY)
        lx = html.fromstring(xmlBODY)

        status_request = lx.xpath('//bs_r/text()')[0]
        print(status_request)


    soup = BeautifulSoup(xmlBODY, 'html.parser')
    for cd in soup.findAll(text=True):
        if isinstance(cd, CData):
            VECTORS.append(cd)

    vector = VECTORS[4]
    print(xmlBODY)
    print(status_request)
    print(vector)






login()
request(WORKINGDIRECTORY[0])
answer(REQUESTNUMDER[0], WORKINGDIRECTORY[0])
#answer('9BS78425371', 'U3870278092')