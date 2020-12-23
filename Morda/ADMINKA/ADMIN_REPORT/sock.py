#
#
# # import websocket
# #
# # ws = websocket.create_connection('ws://127.0.0.1:3342/socket.io/')
# # ws.send({'EIO':'3','transport':'websocket','sid':'4IicFHqqsO6J5r0wAfcJ'})
# # #'http://127.0.0.1:3342/socket.io/?EIO=3&transport=websocket&sid=IOlrDmwz6sbotWsKAeTl')
#
#
#
# from lxml import html
#
# import requests
#
# LOGIN = 'demo'  # 'demo' #'Svetka' #'ander_автомат'
# PASSWORD = 'Gfd!1qaz40'  # 'Gfd!1qaz40' #'153759' #'687dd78R'
# WD = ''
#
# S=requests.Session()
# from http.cookiejar import MozillaCookieJar
# S.cookies = MozillaCookieJar('cookies.txt')
#
# def login():
#     URL = 'http://127.0.0.1:3342/'  # http://vips1/ #https://ips3:888/ #http://127.0.0.1:3333/
#     loginURL = URL + 'login'
#
#
#     post={
#                     'Type': 'Login',
#                     'Login': LOGIN,
#                     'Password': PASSWORD}
#
#     headers = {
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
#         "Connection": "keep-alive",
#         "Content-Length": "32",
#         "Content-Type": "application/x-www-form-urlencoded",
#         "Cookie": "L[login]=demo",
#         #"Host": "http://127.0.0.1:3342",
#         #"Origin": "http://127.0.0.1:3342",
#         #"Referer": "http://127.0.0.1:3342/login",
#         "Upgrade-Insecure-Requests": "1",
#         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
#         #'Sec - WebSocket - Key': 'n4OH2M242b2R7HIEVWslJg =='
#     }
#     cookies = {
#
#     }
#     rPOST = S.post(loginURL, data=post, headers=headers)
#     #print(rPOST.cookies.get_dict())
#     #print(rPOST.headers)
#     S.cookies.save()
#     lx = html.fromstring(rPOST.content)
#     WD = lx.xpath('//sid/text()')[0]
#
#     r = S.get('http://127.0.0.1:3342')
#     #print(r.text)
#     print(S.cookies)
#
#     print('получил WD ' + str(WD))
#
#     url = 'http://127.0.0.1:3342/admin/api/report/settings?'
#     params = 'login[]=4693/17-У&\
#             from=10.12.2019&\
#             to=10.12.2019&\
#             excelTemplate=O4&\
#             price=true'
#     URL = url + params
#     r = S.get(URL)
#     print(r.text)
#
#     if WD == '':
#         print('не получил WD')
#
#     return WD
#
#
#
# print(login())
#
# import socketio
#
# sio = socketio.Client(logger=True, engineio_logger=True)
# sio.connect('http://127.0.0.1:3342/' )
# print('SIO.SID   '+sio.sid)
# print(sio.connected)
# for event in sio.event():
#     print(event)
#
#
#
# # sio.wait()
#
#
# import asyncio
# import websockets
#
# async def responseFunc(uri):
#     async with websockets.connect(uri) as websocket:
#         await websocket.recv()
#
#
# url = "ws://127.0.0.1:3342/socket.io/?EIO=3&transport=websocket&sid=" + 'IOlrDmwz6sbotWsKAeTl'
# print('!!!!!!!!!!!!!!!!!!!')
# asyncio.get_event_loop().run_until_complete(
#     responseFunc(url))


from websocket import create_connection
import json
ws = create_connection("ws://yanik:3080/socket.io/?EIO=3&transport=websocket", ssl=True)# cookie = "csrftoken=DhSf0z9Ouu5f1SbfGWBg5BuBe1UuJMLr; sessionid=pu6ig4z4mtq5k8rvm6kuv8g3fdegs47d")

for event in ws:
    j = json.loads(event[1:])
    print (j['sid'])
    wss = create_connection("ws://127.0.0.1:3342/socket.io/?EIO=3&transport=websocket&sid=syWhSZQ6t7kqzcScAQdT" + str(j['sid']), ssl=True)
    for ev in wss:
        print(ev)



import ssl
import websocket

ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
ws.connect("wss://127.0.0.1:3342/socket.io/?EIO=3&transport=websocket")