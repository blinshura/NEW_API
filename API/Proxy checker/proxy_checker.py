import requests
import random
import string
S = requests.Session()

def getCommand():
    r = S.get('http://ves1:7702?command=get')
    print('get - ' + r.text)

def topicCommand(text):
    r = S.get('http://ves1:7702?command=get&topic={}'.format(text))
    print('topic - {} - '.format(text) + r.text)

def statCommand():
    r = S.get('http://ves1:7702?command=stat')
    print(r.text)

getCommand()
for i in range(1000):
    topicCommand(random.choice(string.ascii_letters))
    getCommand()
