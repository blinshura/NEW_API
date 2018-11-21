import random
from time import sleep

import requests
from bs4 import BeautifulSoup
import requests
import urllib3
urllib3.disable_warnings()

URL = 'https://ips1'
HEADERS = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br'
}
R = requests.Session()
POD = []
NEPOD = []
EXCEPT = []
NEVOSH = []

def login(LOGIN='demo', PASSWORD='Gfd!1qaz40'):

    payloads = {
        'Login': LOGIN,
        'Password': PASSWORD
    }

    try:
        r = R.post(url=URL + '/login', data=payloads, verify=False)
        ANSWER = BeautifulSoup(r.text, 'lxml')

        if ANSWER.find('username') != None and r.status_code == 200:
            login = ANSWER.username.text

            if login == LOGIN:
                print('ВОШЛИ! ПОДТВЕРДИЛИ  Лоин-' + LOGIN + '  Пароль-' + PASSWORD)
                POD.append('Лоин-' + LOGIN + '  Пароль-' + PASSWORD)
                with open('pod.txt', 'a') as pod:
                    pod.write('Лоин-' + LOGIN + '  Пароль-' + PASSWORD + '\n')
            else:
                print('ВОШЛИ! Не подтвердили Лоин-' + LOGIN + '  Пароль-' + PASSWORD)
                NEPOD.append('Лоин-' + LOGIN + '  Пароль-' + PASSWORD)
                with open('nepod.txt', 'a') as nepod:
                    nepod.write('Лоин-' + LOGIN + '  Пароль-' + PASSWORD + '\n')
        else:
            print('НЕ вошли!   Лоин-' + LOGIN + '  Пароль-' + PASSWORD)
            NEVOSH.append('Лоин-' + LOGIN + '  Пароль-' + PASSWORD)
            with open('nevosh.txt', 'a') as nevosh:
                nevosh.write('Лоин-' + LOGIN + '  Пароль-' + PASSWORD + '\n')

    except Exception as e:
        print("возникла проблема")
        EXCEPT.append(e)
        with open('except.txt', 'a') as exc:
            exc.write('Лоин-' + LOGIN + '  Пароль-' + PASSWORD + '\n')



def logout():
    r = R.get(url=URL + '/logout', verify=False)
    #print(r.status_code)









with open('logins.txt',encoding='utf-8', newline='') as logins:
    login_pass = logins.read().split('\n')


a = 0
login_list = {}
for i in login_pass[::2]:
    LOGIN = str(login_pass[a])
    LOGIN = LOGIN.replace('\r', '')
    PASSWORD = str(login_pass[(a + 1)])
    PASSWORD = PASSWORD.replace('\r', '')
    #print('LOGIN:' + LOGIN + ' ' + 'PASSWORD:' + PASSWORD)
    login_list.setdefault(LOGIN, PASSWORD)
    a += 2

for l, p in login_list.items():
    LOGIN = str(l)
    PASSWORD = str(p)
    #print('LOGIN:' + l + ' ' + 'PASSWORD:' + p)
    login(LOGIN, PASSWORD)
    logout()


print('ПОДТВЕРЖДЕНЫ:')
for p in POD:
    print(p)
print('=================================')

print('НЕ подтверждены:')
for np in NEPOD:
    print(np)
print('=================================')

print('НЕ вошли:')
for nv in NEVOSH:
    print(nv)
print('=================================')

print('Ошибки')
for ex in EXCEPT:
    print(ex)
print('=================================')