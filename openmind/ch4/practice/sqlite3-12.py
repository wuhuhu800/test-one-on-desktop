#https://docs.python.org/3/library/sqlite3.html#registering-an-adapter-callable
import sqlite3
class Point:
    def __init__(self, x, y):
        self.x , self.y = x , y
def adapt_point(point):
    return "%.2f;%.2f" %(point.x, point.y)

sqlite3.register_adapter(Point,adapt_point)#这register_adapter两个参数之间传递的原理不理解
con = sqlite3.connect(":memory:")
cur = con.cursor()

p = Point(4.0 , -3.0)

cur.execute("select ?",(p,))
print(cur.fetchone()[0])
