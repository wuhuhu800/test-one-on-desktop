import sqlite3
conn = sqlite3.connect("example.db")
conn.row_factory = sqlite3.Row
c = conn.cursor()
c.execute('select * from stocks')
r = c.fetchone()
for member in r:
    print(member)
