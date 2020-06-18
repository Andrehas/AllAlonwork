import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: ') : continue
    # Your code there
    # Get domain name - org variable
    email = line
    org = line.split("@")[1]
    print org
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (org, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count) 
                VALUES ( ?, 1 )''', ( org, ) )
    else : 
         cur.execute('UPDATE Counts SET count=count+1 WHERE email = ?',
            (org, ))
    # This statement commits outstanding changes to disk each 
    # time through the loop - the program can be made faster 
    # by moving the commit so it runs only after the loop completes
    conn.commit()

# https://www.sqlite.org/lang_select.html
# Your code there
# Make your sql request - get top 10 rows ordered by count
sqlstr = 'SELECT * FROM Counts ORDER BY count DESC LIMIT 10'


print "---------"
for row in cur.execute(sqlstr) :
    print "Counts: "
    print row[0],row[1]
    # Your code there
    # Print domain and count

cur.close()

