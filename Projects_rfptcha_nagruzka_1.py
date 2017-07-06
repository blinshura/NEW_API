import timeit
from datetime import datetime
from grab import Grab, UploadFile
from lxml import html
import threading
from time import sleep

REQUESTS = 10
THREADS = 2  # max 700
URL = '95.31.1.216/in.php'
key = '5821e03012f4a9b272f52740'
file_path = 'C:\\9993_518531.png'

sllep_time = 2  # задеражка запуска потоков
sleep_tread = 2 # задеражка запуска потоков

connect_timeout = 10   #
timeout = 30  # port 80: Timed out
printing = []
ITER = []
Exceptions = []
Exceptionse1 = []
Exceptionse2 = []
IDE = []

a = timeit.default_timer()
def login(iter):
    i = 0


    while i < iter:

        try:
            g = Grab(timeout=timeout, connect_timeout=connect_timeout)
            #g.setup(multipart_post={'body': UploadFile('C:\\9993_518531.png')})
            #g.setup(multipart_post={'foo': 'bar', 'body': UploadFile('C:\\9993_518531.png')})
            go = g.go(URL, multipart_post={'body': UploadFile(file_path), 'key': key})
            lx = html.fromstring(go.body)
            ID = lx.xpath('//text()')
            #print(ID)
            id = ID[0]
            id = id[3:]
            IDE.append(id)
            print(id)
            printing.append(1)
            ITER.append(1)

        except Exception as e1:
            Exceptionse1.append(e1)

        i += 1


def otvet(id, okt):

        try:
            ok = okt
            while ok != 'OK' + okt:

                gg = Grab(timeout=timeout, connect_timeout=connect_timeout)
                go = gg.go('95.31.1.216/res.php?id=' + id + '&key=' + key + '&action=get')
                mxmlBODY = (go.body)
                mx = html.fromstring(mxmlBODY)
                OK = mx.xpath('//text()')
                ok = OK[0]
                ok = ok[:2] + okt
                print(OK[0])
                printing.append(1)

        except Exception as e2:
            Exceptionse2.append(e2)




thread = 0
working_threds =[]
print('ZAPROSI')
try:
    while thread < THREADS:

        t = 't' + str(thread)

        if thread % sleep_tread == 0:
            sleep(sllep_time)

        p = threading.Thread(target=login, name=t, args=[REQUESTS]) # args - количество запросов
        p.start()
        working_threds.append(p)
        thread += 1

except Exception as e:
    Exceptions.append(e)


while len(IDE)==0:
    sleep(1)
print('OTETI')
try:
    for ide in IDE:
        thread = 0
        t = 't' + str(thread)

        if thread % sleep_tread == 0:
            sleep(sllep_time)

        p1 = threading.Thread(target=otvet, name=t, args=[ide, t]) # args - количество запросов
        p1.start()
        working_threds.append(p1)
        thread += 1

except Exception as e:
    Exceptions.append(e)

for wt in working_threds:       # ждем завершения всех потоков
    wt.join()
    #print('thread is joined ' + str(wt))

b = timeit.default_timer()

# Отчет
print('\n')
print('--- Итог теста ---')
print('Кол-во потоков всего: ' + str(len(working_threds)))
print('Отправлено картинок: ' + str(len(ITER)))
total_time = b - a
print('Выполнено обращений к серверу: ' + str(len(printing)))
print('Полное время теста: ' + str(total_time))
request_speed = total_time/len(printing)
print('Средняя скорость обращения: ' + str(request_speed))

print('------ ОШИБКИ ------')

print('Ошибки Потоки : ' + str(len(Exceptions)))
for i in Exceptions:
    print(i)

print('Ошибки Картинка : ' + str(len(Exceptionse1)))
for i1 in Exceptionse1:
    print(i1)

print('Ошибки Ответ : ' + str(len(Exceptionse2)))
for i2 in Exceptionse2:
    print(i2)