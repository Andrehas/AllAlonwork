import json
import urllib

serviceurl = raw_input('Enter location: ')
if not serviceurl: serviceurl = 'https://python-data.dr-chuck.net/comments_283750.json'

print 'Retrieving', serviceurl
uh = urllib.urlopen(serviceurl)
data = uh.read()
js = json.loads(data)
#TODO
#Make dictionary from elements in xml file where: key - name, value - count

#print dictionary
count = []
name = []

for i in js['comments']:
    #print i['name'],i['count']
    name.append(i['name'])
    count.append(i['count'])
templist = []

for j in name:
    templist.append(j)
    for k in range(len(name)+1):
        if name[k] == j:
            count[j] += count[k]
            name.remove(name[k])
dictionary = dict(zip(name,count))

print dictionary