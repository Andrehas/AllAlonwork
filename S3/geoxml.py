import urllib
import xml.etree.ElementTree as ET

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address, 'key':})
    print 'Retrieving', url
    uh = urllib.urlopen(url).read()
    print 'Retrieved',len(uh),'characters'
    print uh
    tree = ET.fromstring(uh)
    #print uh.find('geometry').text
    #TODO
    #Return lat,lng,adress
    for element in tree.iter('location'):
        for child in element:
            print child.text

'''
    print 'lat',lat,'lng',lng
    print location
'''
