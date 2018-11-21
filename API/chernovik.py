import base64
from datetime import datetime
from OpenSSL.crypto import load_certificate, FILETYPE_PEM, FILETYPE_ASN1
import requests
from lxml import html
import urllib3
from poolmanager import PoolManager
from requests.adapters import HTTPAdapter

urllib3.disable_warnings()
import ssl
print (ssl.OPENSSL_VERSION)

URL = 'https://ips3:450'  #ips1: 192.168.0.118:450  vips1: 192.168.0.135:3777
LOGIN = 'release'#'demo' #'Svetka' #'ander_автомат'
PASSWORD = 'release'#'Gfd!1qaz40' #'153759' #'687dd78R'
cert = 'C:\ssl_croinform_ru.cer'
R = requests.Session()
Exceptions = []
ERRORS = []
HEADERS={
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'}
WD = ''
RNs = {}



#print(requests.get('https://www.howsmyssl.com/a/check', verify=False).json()['tls_version'])


with open('C:\ssl_croinform_ru.cer', "r") as my_cert_file:
    my_cert_text = base64.b64decode(my_cert_file.read())
    cert1 = load_certificate(FILETYPE_PEM, my_cert_text)


def login():
    login_start_time = datetime.now()

    post={
                    'Type': 'Login',
                    'Login': LOGIN,
                    'Password': PASSWORD}
    r = R.post(URL,data=post,headers=HEADERS, verify=False, cert=cert1)
    lx = html.fromstring(r.content)
    WD = lx.xpath('//text()')[1]
    print('WD ' + str(WD))

    login_end_time = datetime.now()
    login_total_time = login_end_time - login_start_time
    #print('login_total_time ' + str(login_total_time))
    with open('c:\\log_API.txt','a') as log:
        log.write(str(login_total_time) + ' ' + 'login' + ' ' + WD + '\n')
    return WD


login()