import sqlite3
def dict_factory(cursor,row):
    d = {}

    for idx,col in enumerate (cursor.description):#不明白？？？
        d[col[0]]=row[idx]
        print(d)
    return d
con = sqlite3.connect(":memory:")
con.row_factory= dict_factory#不明白？？？？
cur = con.cursor()
cur.execute("select 1 as a") #不明白？？？
print(cur.fetchone()["a"])
