import sqlite3
con = sqlite3.connect('logindata.db')
cur = con.cursor()
#cur.execute('''create table users (
#  id INTEGER PRIMARY key ,
#  name text not null,
#  password text not NULL)''')
#cur.execute("insert into users values('1','visit','111')")
#cur.execute("insert into users values('2','admin','123')")
m=cur.execute('select * from users')
print(m.fetchall())
con.commit()
con.close()
