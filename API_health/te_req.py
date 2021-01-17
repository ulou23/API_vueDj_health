import requests

res=requests.get("https://api.nfz.gov.pl/app-itl-api/queues?format=json&case=1&province=01&benefitForChild=true&api-version=1.3")

print(res.status_code)
print(res.text)
print(res.json()['data'])
odp=res.json()['data']

for d in odp:
    print(d['attributes']['provider'])
    print(d['attributes']['locality'])
    print(d['attributes']['regon-provider'])
    print(d['attributes']['covid-19'])
    print(d['attributes']['benefit'])