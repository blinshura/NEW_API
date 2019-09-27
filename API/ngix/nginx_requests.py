import requests
from lxml import html

R = requests.Session()
# print(.text)
URL = 'http://ips2:3777/api'
HEADERS={
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'}
LOGIN = 'demo'#'demo' #'Svetka' #'ander_автомат'
PASSWORD = 'Gfd!1qaz40'#'Gfd!1qaz40' #'153759' #'687dd78R'


def login():

    post={
                    'Type': 'Login',
                    'Login': LOGIN,
                    'Password': PASSWORD}
    r = R.post(URL,data=post, headers=HEADERS)
    lx = html.fromstring(r.content)
    WD = lx.xpath('//text()')[1]
    print('получил WD ' + str(WD))
    if WD == '':
        with open('C:\\nginx_log', 'a')as file:
            file.write('не получил WD' + '\n')

    return WD


def logout(WD):

    post={
                            'Type': 'Logout',
                            'WorkingDirectory': WD,
                        }

    r = requests.post(URL, data=post, headers=HEADERS,verify=False,)
    xmlBODY = (r.content)
    lx = html.fromstring(xmlBODY)
    ANS = lx.xpath('//text()')[3]
    print('LOGOUT ' + str(ANS))
    if ANS == '':
        with open('C:\\nginx_log', 'a')as file:
            file.write('не не удалось произвести логаут' + '\n')


for i in range(1000):
    wd = login()
    logout(wd)
