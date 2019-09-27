
import requests
import json

import schedule
import time
# import telebot
# from telebot import apihelper
# from pyrogram import Client
#
# app = Client("794133176:AAGEOXh4r7s4GOHWSLIPhr_faY4uKxuVdkQ")
# app.run()
# with app:
#     app.send_message('sotial_bot','sdow')
#
#ReplyKeyboardRemove
#
#
#
# #apihelper.proxy = {'https': 'socks5://hotgram:221a7ece3c3714@94.101.121.171:443'}
# #apihelper.proxy = {'https':'socks5://userproxy:password@proxy_address:port'}
#                    #94.101.121.171 & port = 443 & user = hotgram &pass=221a7ece3c3714
#
#
#
# # bot_token = '794133176:AAGEOXh4r7s4GOHWSLIPhr_faY4uKxuVdkQ'
# # channel = '@sotial_bot'
# # bot = telebot.TeleBot(bot_token)


url = 'http://portal6:3000/'
headers = {
      "Content-Type" : "application/json",
      "Content-Length" : "post",
    }
data_list = [
{"LastName":"Иванов",
    "FirstName": "Алексей",
    "MaidenName":"Валерьевич",
    "BirthDate":"29.09.1979",
    "City": "",
     "Password": "jztJxSL0Z9l2STHKwScz",
     "UserName": "cronos"},

{"LastName":"Блинов",
    "FirstName": "Дмитрий",
    "MaidenName":"Валерьевич",

    "BirthDate":"15.11.1967",
    "City": "",
     "Password": "jztJxSL0Z9l2STHKwScz",
     "UserName": "cronos"},

{"LastName":"Жданова",
    "FirstName": "Елена",
    "MaidenName":"Михайловна",
    "BirthDate":"05.01.1978",
    "City": "",
     "Password": "jztJxSL0Z9l2STHKwScz",
     "UserName": "cronos"},

# {"LastName":"Владимирская",
#     "FirstName": "Алена",
#     "MaidenName":"",
#     "BirthDate":"",
#     "City": "Москва",
#      "Password": "jztJxSL0Z9l2STHKwScz",
#      "UserName": "cronos"},


]

def job():
    print('Starts at :' + str(time.ctime()))

    for i in data_list:
        data = i

        data = json.dumps(data).encode("utf-8")

        r = requests.post(url, data=data, headers=headers)
        parsed = json.loads(r.text) # str(r.json()["result"])
        parsed = json.dumps(parsed, indent=4, sort_keys=True, ensure_ascii=False)
        print(parsed)
        j = r.json()
        #telbot(j['stats'])
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

    print('#####################' + 'Stop at :' + str(time.ctime()) + '#######################')

job()
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
schedule.every().day.at("10:00").do(job)
# schedule.every(5).to(10).days.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

