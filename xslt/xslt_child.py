

from bs4 import BeautifulSoup
from grab import *
from lxml import html
import requests

ii = [
    'd1093d39-0b91-4dc1-b62e-fabdac9c7be7',
    '0c8c2bab-9a7f-470c-85a8-2a37d13cd133',
    '92206502-98db-4faa-a7fd-07cd4f91bd67',
    '92718b67-05a2-4c36-8703-592b55b788a9',
    'c8ae7cf8-9502-41de-b9b1-b585709c2919',
    '3088ff14-d1f9-449f-b655-b53cd60b2c31',
    '6b68e9fb-a6a3-4a56-8ffc-631d30a1e14f',
    'ff2a85c5-8edd-4c5d-a642-e5a9dc1ba2db',
    '5a780a17-f57a-4e1a-b390-5aab80ca14ab',
    '129aa300-9335-4ab3-bae9-6c63268fc7d6',
    '0eae6d30-7915-445f-baea-e72ef4c97a2c',
    '868fb60a-4cda-4e62-8476-bb932655481d',
    '98b3ad69-5ecd-4370-aaac-8f127a257ed8',
    '1957137a-3805-446e-9b35-0767bbce0aaa',
    '70810d95-7ad5-422f-a2b6-4fbb6b567687',

    'd1093d39-0b91-4dc1-b62e-fabdac9c7be7',
    '0c8c2bab-9a7f-470c-85a8-2a37d13cd133',
    '92206502-98db-4faa-a7fd-07cd4f91bd67',
    '92718b67-05a2-4c36-8703-592b55b788a9',
    'c8ae7cf8-9502-41de-b9b1-b585709c2919',
    '3088ff14-d1f9-449f-b655-b53cd60b2c31',
    '6b68e9fb-a6a3-4a56-8ffc-631d30a1e14f',
    'ff2a85c5-8edd-4c5d-a642-e5a9dc1ba2db',
    '5a780a17-f57a-4e1a-b390-5aab80ca14ab',
    '129aa300-9335-4ab3-bae9-6c63268fc7d6',
    '0eae6d30-7915-445f-baea-e72ef4c97a2c',
    '868fb60a-4cda-4e62-8476-bb932655481d',
    '98b3ad69-5ecd-4370-aaac-8f127a257ed8',
    '1957137a-3805-446e-9b35-0767bbce0aaa',
    '70810d95-7ad5-422f-a2b6-4fbb6b567687',

    'd1093d39-0b91-4dc1-b62e-fabdac9c7be7',
    '0c8c2bab-9a7f-470c-85a8-2a37d13cd133',
    '92206502-98db-4faa-a7fd-07cd4f91bd67',
    '92718b67-05a2-4c36-8703-592b55b788a9',
    'c8ae7cf8-9502-41de-b9b1-b585709c2919',
    '3088ff14-d1f9-449f-b655-b53cd60b2c31',
    '6b68e9fb-a6a3-4a56-8ffc-631d30a1e14f',
    'ff2a85c5-8edd-4c5d-a642-e5a9dc1ba2db',
    '5a780a17-f57a-4e1a-b390-5aab80ca14ab',
    '129aa300-9335-4ab3-bae9-6c63268fc7d6',
    '0eae6d30-7915-445f-baea-e72ef4c97a2c',
    '868fb60a-4cda-4e62-8476-bb932655481d',
    '98b3ad69-5ecd-4370-aaac-8f127a257ed8',
    '1957137a-3805-446e-9b35-0767bbce0aaa',
    '70810d95-7ad5-422f-a2b6-4fbb6b567687',

    'd1093d39-0b91-4dc1-b62e-fabdac9c7be7',
    '0c8c2bab-9a7f-470c-85a8-2a37d13cd133',
    '92206502-98db-4faa-a7fd-07cd4f91bd67',
    '92718b67-05a2-4c36-8703-592b55b788a9',
    'c8ae7cf8-9502-41de-b9b1-b585709c2919',
    '3088ff14-d1f9-449f-b655-b53cd60b2c31',
    '6b68e9fb-a6a3-4a56-8ffc-631d30a1e14f',
    'ff2a85c5-8edd-4c5d-a642-e5a9dc1ba2db',
    '5a780a17-f57a-4e1a-b390-5aab80ca14ab',
    '129aa300-9335-4ab3-bae9-6c63268fc7d6',
    '0eae6d30-7915-445f-baea-e72ef4c97a2c',
    '868fb60a-4cda-4e62-8476-bb932655481d',
    '98b3ad69-5ecd-4370-aaac-8f127a257ed8',
    '1957137a-3805-446e-9b35-0767bbce0aaa',
    '70810d95-7ad5-422f-a2b6-4fbb6b567687',

    'd1093d39-0b91-4dc1-b62e-fabdac9c7be7',
    '0c8c2bab-9a7f-470c-85a8-2a37d13cd133',
    '92206502-98db-4faa-a7fd-07cd4f91bd67',
    '92718b67-05a2-4c36-8703-592b55b788a9',
    'c8ae7cf8-9502-41de-b9b1-b585709c2919',
    '3088ff14-d1f9-449f-b655-b53cd60b2c31',
    '6b68e9fb-a6a3-4a56-8ffc-631d30a1e14f',
    'ff2a85c5-8edd-4c5d-a642-e5a9dc1ba2db',
    '5a780a17-f57a-4e1a-b390-5aab80ca14ab',
    '129aa300-9335-4ab3-bae9-6c63268fc7d6',
    '0eae6d30-7915-445f-baea-e72ef4c97a2c',
    '868fb60a-4cda-4e62-8476-bb932655481d',
    '98b3ad69-5ecd-4370-aaac-8f127a257ed8',
    '1957137a-3805-446e-9b35-0767bbce0aaa',
    '70810d95-7ad5-422f-a2b6-4fbb6b567687',

    'd1093d39-0b91-4dc1-b62e-fabdac9c7be7',
    '0c8c2bab-9a7f-470c-85a8-2a37d13cd133',
    '92206502-98db-4faa-a7fd-07cd4f91bd67',
    '92718b67-05a2-4c36-8703-592b55b788a9',
    'c8ae7cf8-9502-41de-b9b1-b585709c2919',
    '3088ff14-d1f9-449f-b655-b53cd60b2c31',
    '6b68e9fb-a6a3-4a56-8ffc-631d30a1e14f',
    'ff2a85c5-8edd-4c5d-a642-e5a9dc1ba2db',
    '5a780a17-f57a-4e1a-b390-5aab80ca14ab',
    '129aa300-9335-4ab3-bae9-6c63268fc7d6',
    '0eae6d30-7915-445f-baea-e72ef4c97a2c',
    '868fb60a-4cda-4e62-8476-bb932655481d',
    '98b3ad69-5ecd-4370-aaac-8f127a257ed8',
    '1957137a-3805-446e-9b35-0767bbce0aaa',
    '70810d95-7ad5-422f-a2b6-4fbb6b567687',

    'd1093d39-0b91-4dc1-b62e-fabdac9c7be7',
    '0c8c2bab-9a7f-470c-85a8-2a37d13cd133',
    '92206502-98db-4faa-a7fd-07cd4f91bd67',
    '92718b67-05a2-4c36-8703-592b55b788a9',
    'c8ae7cf8-9502-41de-b9b1-b585709c2919',
    '3088ff14-d1f9-449f-b655-b53cd60b2c31',
    '6b68e9fb-a6a3-4a56-8ffc-631d30a1e14f',
    'ff2a85c5-8edd-4c5d-a642-e5a9dc1ba2db',
    '5a780a17-f57a-4e1a-b390-5aab80ca14ab',
    '129aa300-9335-4ab3-bae9-6c63268fc7d6',
    '0eae6d30-7915-445f-baea-e72ef4c97a2c',
    '868fb60a-4cda-4e62-8476-bb932655481d',
    '98b3ad69-5ecd-4370-aaac-8f127a257ed8',
    '1957137a-3805-446e-9b35-0767bbce0aaa',
    '70810d95-7ad5-422f-a2b6-4fbb6b567687',

    'd1093d39-0b91-4dc1-b62e-fabdac9c7be7',
    '0c8c2bab-9a7f-470c-85a8-2a37d13cd133',
    '92206502-98db-4faa-a7fd-07cd4f91bd67',
    '92718b67-05a2-4c36-8703-592b55b788a9',
    'c8ae7cf8-9502-41de-b9b1-b585709c2919',
    '3088ff14-d1f9-449f-b655-b53cd60b2c31',
    '6b68e9fb-a6a3-4a56-8ffc-631d30a1e14f',
    'ff2a85c5-8edd-4c5d-a642-e5a9dc1ba2db',
    '5a780a17-f57a-4e1a-b390-5aab80ca14ab',
    '129aa300-9335-4ab3-bae9-6c63268fc7d6',
    '0eae6d30-7915-445f-baea-e72ef4c97a2c',
    '868fb60a-4cda-4e62-8476-bb932655481d',
    '98b3ad69-5ecd-4370-aaac-8f127a257ed8',
    '1957137a-3805-446e-9b35-0767bbce0aaa',
    '70810d95-7ad5-422f-a2b6-4fbb6b567687',

]



url = 'http://192.168.0.135:80/login'
post= {
                    'Type': 'Login',
                    'Login': 'demo',
                    'Password': 'demo',
                    }
headers= {
                    'Accept-Encoding': 'gzip,deflate',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    }

r = requests.Session()
r.post(url, data=post, headers=headers)
sid = r.cookies['cronos.sid']
print(sid)



cooc = {
    'cronos.sid': sid,
    'L[Login]' : 'demo'
}

# cooc = {'L[Login]': 'demo',
#         'cronos.sid': 's:7iO8owBTlPhuoqCUlbwyN3D2.FDDt3CBUHRQyJaX5DWXhToyP6HETbPYjfu78E/NhzbM'
#         }
m=0
for i in ii:
    r = requests.get('http://192.168.0.135:80/download/UL/HTML/' + i, cookies=cooc)
    print(r.text[115:149] +  '     ' + str(m))
    m+=1




