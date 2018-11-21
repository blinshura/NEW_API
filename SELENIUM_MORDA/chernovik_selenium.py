import random
from time import sleep

import requests
from bs4 import BeautifulSoup
from lxml import html

URL = 'https://ips1'
HEADERS = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br'
}
ID = [
    'd9035116-efd8-4474-b805-b1347322178d',
    '3c6bf084-9245-41a5-b340-85665bdd49b9',
    '61aa6407-004f-450b-a9e1-918358d4904a',
    'ccbf8d1d-ce3a-417e-a6d0-fa9f9885dddb',
    '032d7a18-f6e4-4e46-a0d2-13eaba41638a',
    'e70a7b89-9442-4844-a6ed-a02f9fbb70be',
    'ee370581-3671-42b1-b53b-bae1b20d31e1',
    # 'b84dc31c-84c5-45af-86e7-4171c51f232',
    '329d470b-a67d-41e3-8446-1c37d19ccf4b',
    'e0be5294-8235-4d8f-a489-70ec22d68a2f',
    '4cc0490a-377e-489e-90eb-f8e6ac0a63fc',
    'aab444c7-5fdf-402d-8aba-456131ab0e6f',
    'ac5dfb64-56ef-44d1-b1fc-0139ffde2c23',
    'c19f40bb-556f-4f9f-bb66-04e93966fb94',
    '0508f799-517b-48d5-9664-fb7229772dc1',
    '0484e702-b91e-4363-933f-4bdb1e97c161',
    '4b904b57-4061-4c6e-92c1-14c098facdef',
    'a80f2fa3-4078-43bc-af67-16519c128a72',
    '15f4300f-578b-4d86-b779-bfb3591c1cdc',
    '8a2c3576-7679-4d21-93a3-93cf5ac77843',
    'fa7c2960-04c1-4031-8b71-e62d513d7bc2',
    '6a646bf2-f4f5-42b9-a79f-01ce801e9980',
    'fe75ae8b-c430-40a3-a6db-0d072ae2a07c',

    'd9035116-efd8-4474-b805-b1347322178d',
    '3c6bf084-9245-41a5-b340-85665bdd49b9',
    '61aa6407-004f-450b-a9e1-918358d4904a',
    'ccbf8d1d-ce3a-417e-a6d0-fa9f9885dddb',
    '032d7a18-f6e4-4e46-a0d2-13eaba41638a',
    'e70a7b89-9442-4844-a6ed-a02f9fbb70be',
    'ee370581-3671-42b1-b53b-bae1b20d31e1',
    # 'b84dc31c-84c5-45af-86e7-4171c51f232',
    '329d470b-a67d-41e3-8446-1c37d19ccf4b',
    'e0be5294-8235-4d8f-a489-70ec22d68a2f',
    '4cc0490a-377e-489e-90eb-f8e6ac0a63fc',
    'aab444c7-5fdf-402d-8aba-456131ab0e6f',
    'ac5dfb64-56ef-44d1-b1fc-0139ffde2c23',
    'c19f40bb-556f-4f9f-bb66-04e93966fb94',
    '0508f799-517b-48d5-9664-fb7229772dc1',
    '0484e702-b91e-4363-933f-4bdb1e97c161',
    '4b904b57-4061-4c6e-92c1-14c098facdef',
    'a80f2fa3-4078-43bc-af67-16519c128a72',
    '15f4300f-578b-4d86-b779-bfb3591c1cdc',
    '8a2c3576-7679-4d21-93a3-93cf5ac77843',
    'fa7c2960-04c1-4031-8b71-e62d513d7bc2',
    '6a646bf2-f4f5-42b9-a79f-01ce801e9980',
    'fe75ae8b-c430-40a3-a6db-0d072ae2a07c',

    'd9035116-efd8-4474-b805-b1347322178d',
    '3c6bf084-9245-41a5-b340-85665bdd49b9',
    '61aa6407-004f-450b-a9e1-918358d4904a',
    'ccbf8d1d-ce3a-417e-a6d0-fa9f9885dddb',
    '032d7a18-f6e4-4e46-a0d2-13eaba41638a',
    'e70a7b89-9442-4844-a6ed-a02f9fbb70be',
    'ee370581-3671-42b1-b53b-bae1b20d31e1',
    # 'b84dc31c-84c5-45af-86e7-4171c51f232',
    '329d470b-a67d-41e3-8446-1c37d19ccf4b',
    'e0be5294-8235-4d8f-a489-70ec22d68a2f',
    '4cc0490a-377e-489e-90eb-f8e6ac0a63fc',
    'aab444c7-5fdf-402d-8aba-456131ab0e6f',
    'ac5dfb64-56ef-44d1-b1fc-0139ffde2c23',
    'c19f40bb-556f-4f9f-bb66-04e93966fb94',
    '0508f799-517b-48d5-9664-fb7229772dc1',
    '0484e702-b91e-4363-933f-4bdb1e97c161',
    '4b904b57-4061-4c6e-92c1-14c098facdef',
    'a80f2fa3-4078-43bc-af67-16519c128a72',
    '15f4300f-578b-4d86-b779-bfb3591c1cdc',
    '8a2c3576-7679-4d21-93a3-93cf5ac77843',
    'fa7c2960-04c1-4031-8b71-e62d513d7bc2',
    '6a646bf2-f4f5-42b9-a79f-01ce801e9980',
    'fe75ae8b-c430-40a3-a6db-0d072ae2a07c',

    'd9035116-efd8-4474-b805-b1347322178d',
    '3c6bf084-9245-41a5-b340-85665bdd49b9',
    '61aa6407-004f-450b-a9e1-918358d4904a',
    'ccbf8d1d-ce3a-417e-a6d0-fa9f9885dddb',
    '032d7a18-f6e4-4e46-a0d2-13eaba41638a',
    'e70a7b89-9442-4844-a6ed-a02f9fbb70be',
    'ee370581-3671-42b1-b53b-bae1b20d31e1',
    # 'b84dc31c-84c5-45af-86e7-4171c51f232',
    '329d470b-a67d-41e3-8446-1c37d19ccf4b',
    'e0be5294-8235-4d8f-a489-70ec22d68a2f',
    '4cc0490a-377e-489e-90eb-f8e6ac0a63fc',
    'aab444c7-5fdf-402d-8aba-456131ab0e6f',
    'ac5dfb64-56ef-44d1-b1fc-0139ffde2c23',
    'c19f40bb-556f-4f9f-bb66-04e93966fb94',
    '0508f799-517b-48d5-9664-fb7229772dc1',
    '0484e702-b91e-4363-933f-4bdb1e97c161',
    '4b904b57-4061-4c6e-92c1-14c098facdef',
    'a80f2fa3-4078-43bc-af67-16519c128a72',
    '15f4300f-578b-4d86-b779-bfb3591c1cdc',
    '8a2c3576-7679-4d21-93a3-93cf5ac77843',
    'fa7c2960-04c1-4031-8b71-e62d513d7bc2',
    '6a646bf2-f4f5-42b9-a79f-01ce801e9980',
    'fe75ae8b-c430-40a3-a6db-0d072ae2a07c',

]
R = requests.Session()
POD = []
NEPOD = []
EXCEPT = []

def login(LOGIN='demo', PASSWORD='demo'):

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
            else:
                print('ВОШЛИ! Не подтвердили Лоин-' + LOGIN + '  Пароль-' + PASSWORD)
                NEPOD.append('Лоин-' + LOGIN + '  Пароль-' + PASSWORD)

    except Exception as e:
        print("возникла проблема")
        EXCEPT.append(e)



def logout():
    r = R.get(url='https://ips1/logout', verify=False)
    print(r.status_code)









with open('logins.txt',encoding='utf-8', newline='') as logins:
    login_pass = logins.read().split('\n')
    # print(login_pass)

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

print('Ошибки')
for ex in EXCEPT:
    print(ex)
print('=================================')