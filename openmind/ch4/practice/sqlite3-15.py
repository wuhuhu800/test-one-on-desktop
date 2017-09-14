import sqlite3
class Point:
    def __init__(self,x , y):
        self.x ,self.y = x , y
    def __repr__(self): #方法不理解？？？
        return "(%.2f;%.2f)" %(self.x , self.y)

def adapt_point(point):
    return ("%f;%f"%(point.x, point.y)).encode('ascii')

def convert_point(s):
    x ,y = list(map(float, s.split(b";"))) # map不理解，list也不理解？？？
    return Point(x,y)

sqlite3.register_adapter(Point , adapt_point)
sqlite3.register_converter("point",convert_point)#方法不理解？？？

p = Point(4,-3.2)

con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_COLNAMES)#参数值sqlite3.PARSE_COLNAMES不理解
cur =con.cursor()
cur.execute('create table tess(p)')
cur.execute('insert into tess(p) values(?)',(p,))
cur.execute('select p as "p [point]"from tess') #不理解？？？
print("with column names",cur.fetchone()[0])
cur.close()
con.close()
