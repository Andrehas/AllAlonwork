import xml.etree.ElementTree as ET

serviceurl = ('E:/KNU/course2semestr/codinginGIS/alonwork/S3/comments_283746.xml')
print ('Retrieving', serviceurl)


#TODO
#Find sum in count elements
counter = 0
tree = ET.parse(serviceurl)
root = tree.getroot()
for x in root.findall('comments'):
    for y in x.findall('comment'):
        count = y.find('count').text
        counter += int(count)
print(counter)


