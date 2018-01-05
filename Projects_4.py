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




txt='</tr>'

re1='(<[^>]+>)'	# Tag 1

rg = re.compile(re1,re.IGNORECASE|re.DOTALL)
m = rg.search(txt)
if m:
    tag1=m.group(1)
    txt=txt.replace(tag1, '!')
    print ("("+tag1+")"+"\n")
    print(txt)

