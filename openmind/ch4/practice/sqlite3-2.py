import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()

c.execute('SELECT * FROM stocks WHERE symbol = "IBM"' )
print(c.fetchone())

#purchases=[('2016-10-12','BUY','IBM',1000,45.00),
#            ('2016-3-14','BUY','MFST',1000,75.00),
#            ('2016-04-01','SELL','IBM',500,53.00),
#            ]
#c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)',purchases)

for row in c.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)
