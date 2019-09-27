from time import sleep
import requests
from bs4 import BeautifulSoup
from lxml import html
import re
from datetime import datetime
import time





URL = 'http://vips1:3777/api' #'http://127.0.0.1:3331/api' - випс через stunnel  #ips1: 192.168.0.118:450  vips1: 192.168.0.135:3777
LOGIN = 'demo'#'demo' #'Svetka' #'ander_автомат'
PASSWORD = 'demo'#'Gfd!1qaz40' #'153759' #'687dd78R'
R = requests.Session()
Exceptions = []
ERRORS = []
HEADERS={
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'}
WD = ''
RNs = []
RN = ''


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
    'Seria': '5604',
    'Number': '442897',
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

    'zapros': 'FL-Exp'
}



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
    service['WorkingDirectory'] = WD
    r = requests.post(URL,data=service,headers=HEADERS, verify=False,)
    lx = html.fromstring(r.content)
    RN = lx.xpath('//text()')[1]
    print(RN)
    return RN

def response(WD, RN, service):

    StatusANS = '3'
    StatisticANS = ''
    tryes = 30
    while StatusANS == '3' and tryes >= 1:

        post = {'Type': 'Answer',
                'WorkingDirectory': WD,
                'RequestNumber': RN,
                'TypeAnswer': 'XH',
                }
        post['RequestNumber'] = RN
        post['WorkingDirectory'] = WD
        r = requests.post(URL, data=post, headers=HEADERS, verify=False,)

        # print(r.text[:100])





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


            #print(StatisticANS)

        if StatusANS == '3': sleep(3)

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
        #     for key, value in RNs.items():
        #             resp = response(WD, key, value)
        #             while resp == 'err':
        #                 WD = login()
        #                 sleep(3)
        #                 if WD != 'ERROR_VALIDATION_WORKINGDIRECTORY':
        #                     resp = response(WD, key, value)
        #                     break
        #
        #     it+=1



        # ЕДИНИЧНЫЙ ЗАПРОС

        # service = FLExp # IDFL
        # RN = request(WD, service)
        # response(WD, RN, service)


        # НАГРУЗКА


        service = FLExp
        d = datetime.now().minute + 30
        while datetime.now().minute < d: # выполняем цикл в течение 30 минут
                while datetime.now().minute % 2 != 0: # выполняем сбор RN пока минута нечетная
                    print('Нечетная минута, собираем RN')
                    RN = request(WD, service)
                    RNs.append(RN)
                    sleep(5)

                while datetime.now().minute % 2 == 0: # выполняем проверку ответов, пока минута четная
                    if not RNs: # если список пуст, пропускаем действие
                        pass
                    else: # если не пуст, проверяем ответы
                        for rn in RNs:
                            print('Четная минута, собираем ответы')
                            response(WD, rn, service)
                            sleep(2)
                        RNs.clear()


        logout(WD)

    except Exception as e:
        print(e)