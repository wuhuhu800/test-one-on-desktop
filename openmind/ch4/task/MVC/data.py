import practicetest
import sqlite3
con = sqlite3.connect('weather.db')
cur = con.cursor()
city = ['北京']
weatherday = '多云'
HistoryMessage={}
#cur.execute('''CREATE TABLE WeatherData
#            (City text NOT NULL ,WeatherDay text , WeatherNight text,
#             TemperatureHigh real , TemperatureDailylow real ,
#             WindDirection text , WindScale INTEGER ,
#             PRIMARY KEY (City)) ''')
#cur.execute("INSERT INTO WeatherData(City, WeatherDay) VALUES(?,?)",(city,weatherday))
#cur.execute('UPDATE WeatherData SET WeatherDay = ? where City = ?',(weatherday,city))
#cur.execute('select City, WeatherDay from WeatherData' ) #where City = ”%s“ % city
cur.execute('SELECT * FROM WeatherData WHERE City in ({0})'.format(', '.join('?' for _ in city)), city)
row = cur.fetchall()
#for r in row:
#    HistoryMessage[r[0]]=r[1]#将天气的数据保存在字典里，以便进行查找
#    print(HistoryMessage)

print(row[0][1])
con.commit()
con.close()
