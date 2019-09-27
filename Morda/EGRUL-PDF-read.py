import requests

S = requests.Session()
url = 'https://egrul.nalog.ru/'
data = {
'query': '1057000084283'
}
req = S.post(url, data=data)
Jreq =  req.json()
t = Jreq['t']
print(t)
url = 'https://egrul.nalog.ru/search-result/' + t + '?r=1559126618163&_=1559126618164'
r = S.get(url)
Jreq = r.json()
Jreq = Jreq['rows'][0]['t']
print(Jreq)
url = 'https://egrul.nalog.ru/vyp-download/' + t
headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate, br',
'Referer': 'https://egrul.nalog.ru/index.html',
'Connection': 'keep-alive',
'Cookie': '_ym_uid=1528360027642252894; _ym_d=1547202484; last_visit=1542096695620::1542107495620; _ga=GA1.2.134020049.1532942792; JSESSIONID=A701CB91A17F5A81B4FCAF1103BAB0FC; _ym_isad=2',
'Upgrade-Insecure-Requests': '1'
}
r = S.get(url)
print(r.text)