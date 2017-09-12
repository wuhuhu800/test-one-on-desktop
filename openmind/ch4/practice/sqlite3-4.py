import sqlite3
class MySum(object):
    """docstring for MySum."""
    def __init__(self):
        self.count =0
    def step(self,value):
        self.count += value
    def finalize(self):
        return self.count
con = sqlite3.connect(":memory:")
con.create_aggregate("mysum",1,MySum)
cur = con.cursor()
cur.execute('create table test(i)') #i表示列表的表头
cur.execute('insert into test(i) values (1)')# 1表值为1
cur.execute('insert into test(i) values (2)')
cur.execute('select mysum(i) from test')#这一行不理解？？？？
print (cur.fetchone()[0])#取首值
