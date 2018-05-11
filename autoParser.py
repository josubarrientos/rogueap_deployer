import json

iplist = []

fhand = open('iplist.txt')

for i in fhand.readlines():
    iplist.append(i.strip())

fhand.close()


headers = {'content-type': 'application/json'}

apiCallData = apiCallData = {
    "query":{
        "operator":"all",
        "children":[{
            "field":"session.dst_ip",
            "operator":"is in the list",
            "value":["212.55.8.132","212.55.8.133"]},{
            "field":"session.tstamp",
            "operator":"is after",
            "value":["2018-04-12T00:00:00","2018-05-11T23:59:59"]}]},
    "scope":"private",
    "size":50,
    "from":0,
    "sort":{
        "create_date":{"order":"desc"}}}



apiCallData['query']['children'][0]['value'] = iplist

cadena = json.dumps(apiCallData)

fhand = open('queryDataString.json','w')

fhand.write(cadena)

fhand.close()