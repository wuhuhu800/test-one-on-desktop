import practicetest
import sqlite3
con = sqlite3.connect('weather.db')
cur = con.cursor()
city = ['北京']
#UserInputCity = input('请输入所要查询的城市>>>')
ListForCompare =[]
weatherday = '多云'
cur.execute('SELECT * FROM WeatherData WHERE City in ({0})'.format(', '.join('?' for _ in city)), city)
# 上面这句查询语句作用就是能把一横行的数据都查出来
row = cur.fetchall()
if row == ListForCompare:#如果没有查询的内容为空的话
    print(1)

#    1、调用接口查数据
#    2、查到数据保存在数据库里。
else:
    print(row)

#    pass 1、返回要查的内容
#    2、每隔3小时查询一次数据库，并且更新数pass据库
#HistoryMessage={}
#cur.execute('''CREATE TABLE WeatherData

#            (City text NOT NULL ,WeatherDay text , WeatherNight text,
#             TemperatureHigh real , TemperatureDailylow real ,
#             WindDirection text , WindScale INTEGER ,
#             PRIMARY KEY (City)) ''')
#cur.execute("INSERT INTO WeatherData(City, WeatherDay) VALUES(?,?)",(city,weatherday))
#cur.execute('UPDATE WeatherData SET WeatherDay = ? where City = ?',(weatherday,city))
#cur.execute('select City, WeatherDay from WeatherData' ) #where City = ”%s“ % city
#cur.execute('SELECT * FROM WeatherData WHERE City in ({0})'.format(', '.join('?' for _ in city)), city)
# 上面这句查询语句作用就是能把一横行的数据都查出来
#row = cur.fetchall()
#for r in row:
#    HistoryMessage[r[0]]=r[1]#将天气的数据保存在字典里，以便进行查找
#    print(HistoryMessage)


con.commit()
con.close()
