import json
import urllib

serviceurl = raw_input('Enter location: ')
if not serviceurl: serviceurl = 'https://python-data.dr-chuck.net/comments_42.json'
#if not serviceurl: serviceurl = 'https://python-data.dr-chuck.net/comments_283750.json'

print 'Retrieving', serviceurl
uh = urllib.urlopen(serviceurl)
data = uh.read()
js = json.loads(data)
#TODO
#Find sum of comments
count = 0
suma = 0

for i in js['comments']:
    suma += i['count']
    count += 1
print suma,count


