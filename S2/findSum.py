# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program
import urllib
from BeautifulSoup import *
def findSum(url,tag):
    '''
     '    Returns amount of all numbers in the input url file. Ignores letters, non-characters\n'
     '    like punctuation and spaces.\n'
     '\n'
     '    url: url path to input file\n'
     '    tag: tag where the numbers are\n'
     '    returns: sum of all numbers\n')
    '''
    site = urllib.urlopen(url).read()
    soup = BeautifulSoup(site)
    number = 0
    for record in soup.findAll(tag, "comments"):
        number +=int(record.text)
    print number

if __name__ == '__main__':
    # To test findSum:
    
    test1 = findSum("file:///E:/KNU/course2semestr/codinginGIS/alonwork/S2/comments_42.html",'span')
    if '2' == str(test1)[0] and '3' == str(test1)[3]:
        print ("1. Amount of test 1 is: " + str(test1))

    test2 = findSum("file:///E:/KNU/course2semestr/codinginGIS/alonwork/S2/comments_283749.html",'span')
    if '3' == str(test2)[1] and '8' == str(test2)[3]:
        print ("1. Amount of test 2 is: " + str(test2))
