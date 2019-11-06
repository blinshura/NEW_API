import requests
from lxml import html
import json

LOGIN = 'demo'#'demo' #'Svetka' #'ander_автомат'
PASSWORD = 'Gfd!1qaz40'#'Gfd!1qaz40' #'153759' #'687dd78R'
URL = 'http://vips1:999/'
loginURL = URL + 'login'
adminURL = URL + 'admin/api/user/info?login[]=demo'
pushURL = URL +  'admin/api/user/info'

WD = ''
ERRORS = []
S = requests.Session()
headers = {
        'Accept': 'application / json, text / javascript, * / *; q = 0.01',
        'Accept - Encoding': 'gzip, deflate, br',
        'X - Requested - With': 'XMLHttpRequest',
        'Content - Type': 'application / x - www - form - urlencoded;charset = UTF - 8'
    }


def login():


    post={
                    'Type': 'Login',
                    'Login': LOGIN,
                    'Password': PASSWORD}
    rPOST = S.post(loginURL,data=post, )
    print(rPOST.text)
    lx = html.fromstring(rPOST.content)
    WD = lx.xpath('//sid/text()')[0]

    print('получил WD ' + str(WD))
    if WD == '':
        print('не получил WD')
    with open('C:\PycharmProjects\dom3-5-2\\rabota\morda boevaya\ADMINKA\WD\WD.txt', 'w') as wd:
        wd.write(WD)
    return WD

def admin_demo():

    rGET = S.get(adminURL, headers=headers)
    print(json.dumps(rGET.json(), indent=2))

def push_admin_data():
    with open('C:\PycharmProjects\dom3-5-2\\rabota\morda boevaya\ADMINKA\\admin data\\admin_data.json') as file:
        line = json.load(file)
        line['user[billingType]'] = 'MONEY'
        print(line)
        post = line
        print(pushURL)
        r = S.post(pushURL, data=post, headers=headers)
        print(r.text)

if __name__ == '__main__':
    login()
    # admin_demo()
    push_admin_data()