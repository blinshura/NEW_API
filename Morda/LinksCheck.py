from datetime import datetime
from lxml import html

import requests
from pyquery import PyQuery

URL = 'http://vips1:3081/' #'http://127.0.0.1:3331/api' - випс через stunnel  #ips1: 192.168.0.118:450  vips1: 192.168.0.135:3777
LOGIN = 'demo'#'demo' #'Svetka' #'ander_автомат'
PASSWORD = 'demo'#'Gfd!1qaz40' #'153759' #'687dd78R'
R = requests.Session()
HEADERS={
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'}
ERRs=[]

urls = [
'http://vips1:3081/api/billing/UL?_=1553845792799',
'http://vips1:3081/api/request?from=01.01.2019&to=29.03.2019&subSystem=UL&_=1553845792800',
'http://vips1:3081/api/request?from=01.01.2019&to=29.03.2019&subSystem=&_=1553845792801',
'http://vips1:3081/api/request?from=19.03.2019&to=29.03.2019&subSystem=&_=1553845792806',
'http://vips1:3081/api/request?cursor=has&_=1553845792802',
'http://vips1:3081/api/request?cursor=has&_=1553845792803',
'http://vips1:3081/api/request?cursor=has&_=1553845792804',
'http://vips1:3081/api/request?cursor=has&_=1553845792805',

'http://vips1:3081/api/billing/FL?_=1553845792807',
'http://vips1:3081/api/request?from=19.03.2019&to=29.03.2019&subSystem=FL&_=1553845792808',
'http://vips1:3081/api/request?from=19.03.2019&to=29.03.2019&subSystem=&_=1553845792809',
'http://vips1:3081/api/request?from=01.03.2019&to=29.03.2019&subSystem=&_=1553845792810',
'http://vips1:3081/api/request?cursor=has&_=1553845792811',
'http://vips1:3081/api/request?cursor=has&_=1553845792812',
'http://vips1:3081/api/request?cursor=has&_=1553845792813',

'http://vips1:3081/api/billing/IP?_=1553845792814',
'http://vips1:3081/api/request?from=01.03.2019&to=29.03.2019&subSystem=IP&_=1553845792815',
'http://vips1:3081/api/request?from=01.03.2019&to=29.03.2019&subSystem=&_=1553845792816',
'http://vips1:3081/api/request?from=01.01.2019&to=29.03.2019&subSystem=&_=1553845792817',
'http://vips1:3081/api/request?cursor=has&_=1553845792818',
'http://vips1:3081/api/request?cursor=has&_=1553845792819',
'http://vips1:3081/api/request?cursor=has&_=1553845792820',


'http://vips1:3081/api/billing/UP?_=1553845792821',
'http://vips1:3081/api/request?from=01.01.2019&to=29.03.2019&subSystem=UP&_=1553845792822',
'http://vips1:3081/api/request?from=01.02.2019&to=28.02.2019&subSystem=&_=1553848755629',
'http://vips1:3081/api/request?cursor=has&_=1553848830163',
'http://vips1:3081/api/request?cursor=has&_=1553848830164',
'http://vips1:3081/api/request?cursor=has&_=1553848830165',

'http://vips1:3081/api/billing/TS?_=1553848830167',
'http://vips1:3081/api/request?from=01.02.2019&to=28.02.2019&subSystem=TS&_=1553848830168',
'http://vips1:3081/api/request?cursor=has&_=1553848830170',
'http://vips1:3081/api/request?cursor=has&_=1553848830172',
'http://vips1:3081/api/request?cursor=has&_=1553848830173',

'http://vips1:3081/api/billing/PH?_=1553848830174',
'http://vips1:3081/api/request?from=19.03.2019&to=29.03.2019&subSystem=PH&_=1553848830175',
'http://vips1:3081/api/request?from=19.03.2019&to=29.03.2019&subSystem=&_=1553848830176',
'http://vips1:3081/api/request?cursor=has&_=1553848830177',
'http://vips1:3081/api/request?cursor=has&_=1553848830178',

'http://vips1:3081/api/billing/AD?_=1553848830179',
'http://vips1:3081/api/request?from=19.03.2019&to=29.03.2019&subSystem=AD&_=1553848830180',
'http://vips1:3081/api/request?from=01.01.2019&to=29.03.2019&subSystem=AD&_=1553848830181',

'http://vips1:3081/monitoring',
'http://vips1:3081/monitoring/api/billing/IP?_=1553849996246',
'http://vips1:3081/monitoring/api/data?subSystem=UL&_=1553849996249',
'http://vips1:3081/monitoring/api/billing/UL?_=1553849996248',
'http://vips1:3081/monitoring/api/billing/FL?_=1553849996255',
'http://vips1:3081/monitoring/api/data?subSystem=FL&_=1553849996256',
'http://vips1:3081/monitoring/api/data?_=1553849996257',
'http://vips1:3081/monitoring/api/data?subSystem=IP&_=1553849996259',
'http://vips1:3081/monitoring/api/reports/archive/IP?_=1553849996260',

'http://vips1:3081/admin',
'http://vips1:3081/admin/api/rate?id=S1&_=1553850170649',
'http://vips1:3081/admin/api/user/info?login[]=demo&_=1553850170652',
'http://vips1:3081/admin/api/user/history?login=demo&_=1553850170653',
'http://vips1:3081/admin/api/rate?id=S1&_=1553850170654',
'http://vips1:3081/admin/api/user/search?query=demo&blocked=true&_=1553850170655',
'http://vips1:3081/admin/api/user/search?query=demo&blocked=true&overdraft=true&_=1553850170656',
'http://vips1:3081/admin/api/user/search?query=demo&blocked=true&overdraft=true&notification=true&_=1553850170657',
'http://vips1:3081/admin/api/user/search?query=demo&blocked=true&overdraft=true&notification=true&demo=true&_=1553850170658',
'http://vips1:3081/admin/api/user/search?query=demo&blocked=true&overdraft=true&api=true&notification=true&demo=true&_=1553850170659',
'http://vips1:3081/admin/api/user/search?query=demo&blockDate=true&blocked=true&overdraft=true&noContract=true&api=true&notification=true&demo=true&_=1553850170661',


]


def login():

    post={

                    'Login': LOGIN,
                    'Password': PASSWORD}
    r = R.post(URL + 'login',data=post, headers=HEADERS,  verify=False)

    if r.status_code == 200: print('LOGIN status %s' %r.status_code)
    else: print('LOGIN status %s' %'err')

def request(url):
    r = R.get(url)
    if r.status_code == 200: print('REQUEST status %s' %r.status_code)
    else: print('REQUEST status %s' %'err'), ERRs.append(url + ' - ' + 'REQUEST status %s' %'err')


login()
for n in range(1,101):
    print(n)
    for i in urls:
        request(i)

for e in ERRs:
    print(e)
