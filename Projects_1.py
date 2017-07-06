import urllib
import re
import requests


class Auth(object):
    URL = 'http://ips2:777/api.php'



    def auth(self):
        session = requests.Session()
        url = self.URL
        params = {
            'Type': 'Login',
            'Login': 'Test_61959959',
            'Password': '5253325'

        }
        r = session.post(url, params)
        print(r.text)

        urlLibOpenUrl = urllib.request.urlopen( url )
        html = urlLibOpenUrl.read( )
        header_tags = re.findall( r' <WorkingDirectory> (.*?) </WorkingDirectory> ', str(html))
        print( str( '\n'.join( header_tags ) ) )
        ht = html.xpath('//WorkingDirectory')
        print(ht)



if __name__ == '__main__':
    yandex = Auth()
    yandex.auth()