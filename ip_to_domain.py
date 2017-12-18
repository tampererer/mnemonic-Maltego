from MaltegoTransform import *
import requests
import re

me = MaltegoTransform()
ip = sys.argv[1]

response = requests.get('https://api.mnemonic.no/pdns/v3/' + ip + '?limit=100')
response = response.json()

list = response['data']

for index,value in enumerate(list):
    i = value.get('query')
    me.addEntity("maltego.Domain", i)

me.returnOutput()



