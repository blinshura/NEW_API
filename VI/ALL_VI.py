import json
import socket
import base64


import schedule
import time



def croBotSend(bugText):
    print('Отправляем в кробот')
    sock = socket.socket()
    try:
        sock.connect(('192.168.0.39', 8085))
        message = {
            'type': 'publish',
            'topic': 'vi_test',
            'message': bugText
        }

        jMessage = json.dumps(message)
        data = jMessage.encode(encoding='cp1251')
        data = base64.b64encode(data)
        sock.send(data)
        sock.send(bytes('\r\n'.encode(encoding='cp1251')))
        print('Отправили')
        data = sock.recv(1024)
        if not data:
            print("No data")
            sock.close()
        else:
            print(data)
            sock.close()

    except Exception as e:
        print(e)


def job():
    print('Starts at :' + str(time.ctime()))

    text = ''
    from VI import VI_UL_fromList
    for i in VI_UL_fromList.STATUSbug:
        print('UL   ' + i)
        text += ('UL   ' + i + '\n' + '\n')



    from VI import VI_IP_fromList
    for i in VI_IP_fromList.STATUSbug:
        print('IP   ' + i)
        text += ('IP   ' + i + '\n' + '\n')

    from VI import VI_FL_fromList
    for i in VI_FL_fromList.STATUSbug:
        print('FL   ' + i)
        text += ('FL   ' + i + '\n' + '\n')

    print(text)
    croBotSend(text)

#job()

# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
schedule.every().day.at("10:51").do(job)
# schedule.every(5).to(10).days.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
