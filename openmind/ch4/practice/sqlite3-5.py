import sqlite3
def collate_reverse(string1,string2):
    if string1 == string2:
        return 0
    elif string1 < string2:
        return 1
    else:
        return -1

con = sqlite3.connect(":memory:")
con.create_collation("reverse",collate_reverse)
cur = con.cursor()
cur.execute("create table test1(x)")
cur.executemany("insert into test1(x) values (?)",[("a",),("b",)])
cur.execute("select x from test1 order by x collate reverse")
for row in cur:
    print(row)
print(con.set_authorizer(str))

con.close()
