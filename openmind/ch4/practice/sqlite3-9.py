import sqlite3
import string
def char_generator():
    for c in string.ascii_uppercase:
        print(c)
        yield (c,)

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("create table character(c)")

cur.executemany("insert into character(c) values(?)",char_generator())
cur.execute("select y from character")
print(cur.fetchmany(4))
print(cur.rowcount)
print(cur.description)
