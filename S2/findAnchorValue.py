# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *


def findAnchorValue(url, count, position):
    """
    Returns value in anchor in same position after count redirects.

    url: url path to input file
    count: the number of redirects
    position: position for redirects and final value in <a> after count redirects
    """

    for index in xrange(count + 1):
        if index != count:
            html = urllib.urlopen(url).read()
            soup = BeautifulSoup(html)
            # Retrieve all of the anchor tags
            ### TODO
            temp = []
            for record in soup.findAll('a'):
                temp.append(record.text)
            tempurl = "http://python-data.dr-chuck.net/known_by_" + temp[count] + ".html"
        print "Retrieving: " + tempurl
    for index in xrange(count + 1):
        if index != position:
            html1 = urllib.urlopen(tempurl).read()
            soup1 = BeautifulSoup(html1)
            temps = []
            for record in soup1.findAll('a'):
                temps.append(record.text)
    return temps[position]


# DON'T FOGET TO CHANGE THE PATH TO FILES (OISIN, FIKRET) IN YOUR SYSTEM
if __name__ == '__main__':
    # To test findAnchorValue:
    print ("TEST1")
    test1 = findAnchorValue("file:///E:/KNU/course2semestr/codinginGIS/alonwork/S2/known_by_Oisin.html", 2, 2)
    if 'V' == test1[0] and 't' == test1[5]:
        print ("1. Value in anchor on 2 position after 2 redirects is: ") + test1
        print ("+++++++++++++++++++++++++++++++++++++++++++++\n")
        print ("TEST2")
    test2 = findAnchorValue("file:///E:/KNU/course2semestr/codinginGIS/alonwork/S2/known_by_Oisin.html", 5, 2)
    if 'e' == test2[1] and 'n' == test2[4]:
        print ("2. Value in anchor on 2 position after 5 redirects is: ") + test2
        print ("+++++++++++++++++++++++++++++++++++++++++++++\n")
        print ("TEST3")
    test3 = findAnchorValue("file:///E:/KNU/course2semestr/codinginGIS/alonwork/S2/known_by_Fikret.html", 4, 6)
    if 'o' == test3[1] and 'a' == test3[3]:
        print ("3. Value in anchor on 6 position after 4 redirects is: " )+ test3
        print( "+++++++++++++++++++++++++++++++++++++++++++++\n")
        print ("TEST4")
    test4 = findAnchorValue("file:///E:/KNU/course2semestr/codinginGIS/alonwork/S2/known_by_Fikret.html", 11, 2)
    if 'r' == test4[2] and 'e' == test4[4]:
        print ("4. Value in anchor on 2 position after 11 redirects is: ") + test4
        print ("+++++++++++++++++++++++++++++++++++++++++++++\n")
