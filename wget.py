from urllib import request
from urllib.request import Request, urlopen
import json

#print('Skriv inn associationID (1-25): ')
#aID = input()

#print('Skriv inn dato i formatet YYYY-MM-DD: ')
#date = input()

#url = "https://www.varmlandsff.se/api/matches-today/games/?associationId="+aID+"&date="+date
url = "https://www.varmlandsff.se/api/matches-today/games/?associationId=19&date=2022-12-07"
request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
webpage = urlopen(request_site).read()
#print(webpage[:500])

dekodet_json = json.loads(webpage)
#print()
print ("JSON string = ", json.dumps(dekodet_json, indent=4))
print (dekodet_json.keys())
print()
print(dekodet_json['date'])
print()