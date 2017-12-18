from MaltegoTransform import *
import requests
import re

me = MaltegoTransform()
domain = sys.argv[1]

response = requests.get('https://api.mnemonic.no/pdns/v3/' + domain + '?limit=100')
response = response.json()

list = response['data']

for index,value in enumerate(list):
    i = value.get('answer')
    if re.compile("[0-9]+\.[0-9]+\.[0-9]+\.[0-9]").search(i):
        me.addEntity("maltego.IPv4Address", i)

me.returnOutput()



