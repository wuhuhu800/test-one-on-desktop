import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
#c.execute('''CREATE TABLE stocks
#            (data text ,trans text , symbol text, qty real , price real ) ''')
c.execute("INSERT INTO stocks VALUES('2016-06-09','BUY','RHAT',100,35.14)")
conn.commit()
conn.close()
