import requests
from lxml import html

LOGIN = 'demo'  # 'demo' #'Svetka' #'ander_автомат'
PASSWORD = 'Gfd!1qaz40'  # 'Gfd!1qaz40' #'153759' #'687dd78R'
WD = ''

S=requests.Session()



def login():
    URL = 'http://127.0.0.1:3342/'  # http://vips1/ #https://ips3:888/ #http://127.0.0.1:3333/
    loginURL = URL + 'login'


    post={
                    'Type': 'Login',
                    'Login': LOGIN,
                    'Password': PASSWORD}

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "Connection": "keep-alive",
        "Content-Length": "32",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "L[login]=demo; R[subsystem]=FL; newsDate=Wed%20Dec%2011%202019%2015%3A45%3A07%20GMT%2B0300%20(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%20%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5%20%D0%B2%D1%80%D0%B5%D0%BC%D1%8F); newsImpDate=Thu%20Dec%2012%202019%2012%3A57%3A34%20GMT%2B0300%20(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%20%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5%20%D0%B2%D1%80%D0%B5%D0%BC%D1%8F); A[tabId]=%23tab_reports; A[userReportsFormData]=%7B%22from%22%3A%2210.12.2019%22%2C%22to%22%3A%2210.12.2019%22%2C%22excelTemplate%22%3A%22O4%22%2C%22zeroStrings%22%3A%22true%22%2C%22price%22%3A%22true%22%7D; A[tabReportsId]=%23tab_reports-user; cronos.sid=s%3AvfCSwSJEr1HbIF7L63OA9cii.Aorv8e0GgE0JhQkqeMZwKqA%2BWaYp0QvWxiATB44tET4; io=v88cn8_U-rQuOwD3BFek; L[page]=https%3A%2F%2F192.168.0.166%3A888%2F",
        "Host": "192.168.0.166:888",
        "Origin": "http://127.0.0.1:3342",
        "Referer": "http://127.0.0.1:3342/login",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"
    }
    cookies = {

    }
    rPOST = S.post(loginURL,data=post)
    print(S.cookies.get_dict())
    print(rPOST.headers)
    lx = html.fromstring(rPOST.content)
    WD = lx.xpath('//sid/text()')[0]

    r = S.get('http://127.0.0.1:3342')
    #print(r.text)
    #print(S.cookies.get_dict())

    print('получил WD ' + str(WD))
    if WD == '':
        print('не получил WD')

    return WD

def get_report():
    headers = {

            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://192.168.0.166:888/admin",
            "Connection": "keep - alive"
    }
    url = 'http://127.0.0.1:3342/admin/api/report/user?'
    params = 'login[]=4693/17-У&\
    from=10.12.2019&\
    to=10.12.2019&\
    excelTemplate=O4&\
    price=true'
    data = {
        'login[]':'4693%17-У',
            'from':'10.12.2019',
            'to':'10.12.2019',
            'excelTemplate':'O4',
            'price':'true'
    }
    URL = url + params
    r = S.get(URL, )
    #print(r.json())
    url = 'http://127.0.0.1:3342/admin/api/report/settings?'
    params = 'login[]=4693/17-У&\
        from=10.12.2019&\
        to=10.12.2019&\
        excelTemplate=O4&\
        price=true'
    URL = url + params
    r = S.get(URL, )
    #print(S.cookies.get_dict())
    #print(r.text)
    headers = {
    'Accept': '*/*',
    'Connection': 'Upgrade',
    'Pragma': 'no - cache',
    'Cache - Control': 'no - cache',

    'Upgrade': 'websocket',

    'Sec - WebSocket - Version': '13',
    'Accept - Encoding': 'gzip, deflate, brAccept - Language: ru - RU, ru;q = 0.9, en - US;q = 0.8, en;q = 0.7',
    'Cookie': 'cronos.sid=s%3AvfCSwSJEr1HbIF7L63OA9cii.Aorv8e0GgE0JhQkqeMZwKqA%2BWaYp0QvWxiATB44tET4; L[login]=demo; R[subsystem]=FL; io=IOlrDmwz6sbotWsKAeTl; L[page]=https%3A%2F%2F192.168.0.166%3A888%2F; newsDate=Wed%20Dec%2011%202019%2015%3A45%3A07%20GMT%2B0300%20(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%20%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5%20%D0%B2%D1%80%D0%B5%D0%BC%D1%8F); newsImpDate=Thu%20Dec%2012%202019%2012%3A57%3A34%20GMT%2B0300%20(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%20%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5%20%D0%B2%D1%80%D0%B5%D0%BC%D1%8F); A[tabId]=%23tab_reports; A[userReportsFormData]=%7B%22from%22%3A%2210.12.2019%22%2C%22to%22%3A%2210.12.2019%22%2C%22excelTemplate%22%3A%22O4%22%2C%22zeroStrings%22%3A%22true%22%2C%22price%22%3A%22true%22%7D; A[tabReportsId]=%23tab_reports-user; page=https%3A%2F%2F192.168.0.166%3A888%2Fadmin',
    'Sec - WebSocket - Key': 'yDTeyJ2ilHeIihRjGEfAjg==',
    'Sec - WebSocket - Extensions': 'permessage - deflate;client_max_window_bits'
    }
    r = S.get('http://127.0.0.1:3342/socket.io/?EIO=3&transport=websocket&sid=kkIiHvAkHWdu_MUMAgCZ', )
    #print(r.text)
    #print(S.cookies.get_dict())

login()
get_report()