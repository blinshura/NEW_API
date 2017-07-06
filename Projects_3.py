import requests
import lxml
from lxml import html
from selenium import webdriver


Url = 'http://ips2:777/api.php'
session = requests.Session()

headers= {
            'Accept-Encoding': 'gzip,deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': '47',
            'Host': "ips2:777",
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'

            }

data= {
            'Type': 'Login',
            'Login': 'Test_61959959',
            'Password': '5253325'
            }

r = session.post(Url, data)
print (r.text)
m = html.fromstring(r.text.encode('b'))

print(m)
m = r.xpath('.//text()')[1]