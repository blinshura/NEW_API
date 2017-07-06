from datetime import datetime
from grab import *
from lxml import html
import threading
from time import sleep


# g = Grab(timeout=1000, connect_timeout=30)
# go = g.go('95.31.1.216/res.php?id=589aee3fa5d0ed1070637a8f&key=5821e03012f4a9b272f52740&action=get')
# xmlBODY = (go.body)
# lx = html.fromstring(xmlBODY)
#
# ok = lx.xpath('//text()')
# print(ok)

URL = '95.31.1.216/in.php'
key = '5821e03012f4a9b272f52740'
file_path = 'C:\\9993_518531.png'
printing = []
Exceptionse1 = []
def login(iter):
    i = 0


    while i < iter:

            g = Grab(timeout=10, connect_timeout=30)
            go = g.go('95.31.1.216/res.php?id=589aee3fa5d0ed1070637a8f&key=5821e03012f4a9b272f52740&action=get')
            xmlBODY = (go.body)
            lx = html.fromstring(xmlBODY)

            ok = lx.xpath('//text()')
            print(ok)


        # id = 0
        # try:
        #     g = Grab(timeout=10, connect_timeout=30)
        #     #g.setup(multipart_post={'body': UploadFile('C:\\9993_518531.png')})
        #     #g.setup(multipart_post={'foo': 'bar', 'body': UploadFile('C:\\9993_518531.png')})
        #     go = g.go(URL, multipart_post={'body': UploadFile(file_path), 'key': key})
        #     lx = html.fromstring(go.body)
        #     ID = lx.xpath('//text()')
        #     #print(ID)
        #     id = ID[0]
        #     id = id[3:]
        #
        #     print(id)
        #     printing.append(1)
            i += 1





thread = 0

while thread < 100:

    t = 't' + str(thread)

    # if thread % 100 == 0:
    #     sleep(5)

    p = threading.Thread(target=login, name=t, args=[100])  # args - количество запросов
    p.start()

    thread += 1