from grab import Grab
from lxml import html
URL = '192.168.0.50:3777'
g = Grab(timeout=1000, connect_timeout=30)
g.setup(post= {
                    'Type': 'Login',
                    'Login': 'kdinisv',
                    'Password': '123',
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


