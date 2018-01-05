import re
from grab import Grab
from lxml import html
URL = '192.168.0.50:3777'
g = Grab(timeout=1000, connect_timeout=30)
g.setup(post= {
                    'Type': 'Login',
                    'Login': 'demo',
                    'Password': 'demo',
                    },
                    headers= {
                    'Accept-Encoding': 'gzip,deflate',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    }
            )
go = g.go(URL)
#print(g.xpath_text(PATH))
xmlBODY = (go.body)
lx = html.fromstring(xmlBODY)
WD = lx.xpath('//text()')[1]
print('WD ' + str(WD))








FLCASBR = {'Type': 'Request',
                        'WorkingDirectory' : WD,
                        'Event' : '3',
                        'CASBR': '1',
                        'SurName' : 'ХРОМОВ',
                        'FirstName' : 'АЛЕКСАНДР',
                        'MiddleName' : 'ВАЛЕРИАНОВИЧ',
                        'DateOfBirth' :'03.08.1969',
                        'Seria'	: '3213',
                        'Number' : '321321',
                       'zapros': 'FL-CASBR'}