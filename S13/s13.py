import numpy as np

def modelMatrix(inMatrix, sequence):

    v = np.append(np.array(inMatrix['V']), 1)
    v = np.matrix([v]).transpose()
    tempR = inMatrix['R']
    tempT = inMatrix['S']
    tempt2 = inMatrix['T']
    r = np.matrix([[np.cos(np.radians(tempR)), -np.sin(np.radians(tempR)), 0], [np.sin(np.radians(tempR)), np.cos(np.radians(tempR)), 0],
         [0, 0, 1]])
    s = np.matrix([[tempT[0], 0, 0], [0, tempT[1], 0], [0, 0, 1]])
    t = np.matrix([[1, 0, tempt2[0]], [0, 1, tempt2[1]], [0, 0, 1]])
    dictmatrix = {'R': r, 'T': t, 'S': s}
    vect = 1
    for i in sequence:
        matr = dictmatrix[i]
        vect = vect*matr
    outvector = np.ravel(vect*v)
    outtuple = (outvector[0], outvector[1], outvector[2])
    return outtuple

if __name__ == '__main__':

    inMatrix1 = {'R':(33),'T':(1.0,2.0),'S':(2.0,1.2),'V':(1,2)}
    inMatrix2 = {'R':(16),'T':(1.0,2.0),'S':(1.0,2.0),'V':(1,2)}

    firstTest = modelMatrix(inMatrix1,'SRT')
    if -1.05 <= firstTest[0] and -0.95 >= firstTest[0] and 5.25 <= firstTest[1] and 5.4 >= firstTest[1]:
        print "1. 'R':(33),'T':(1.0,2.0),'S':(2.0,1.2),'V':(1,2)" + " Result is: " + str(firstTest)
        print "Test 1 was succesful"

    secondTest = modelMatrix(inMatrix2,'TRS')
    if 0.8 <= secondTest[0] and 0.91 >= secondTest[0] and 6.06 <= secondTest[1] and 6.18 >= secondTest[1]:
        print "2. 'R':(33),'T':(1.0,2.0),'S':(2.0,1.2),'V':(1,2)" + " Result is: " + str(secondTest)
        print "Test 2 was succesful"