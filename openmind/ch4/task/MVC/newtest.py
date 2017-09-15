import practicetest
import sqlite3
import time
con = sqlite3.connect('weather3.db')
cur = con.cursor()
#以下是创建数据表
city ="哈尔滨"
weatherday='雪'
cur.execute('''CREATE TABLE WeatherData

            (City text NOT NULL ,WeatherDay text , WeatherNight text,
             TemperatureHigh real , TemperatureDailylow real ,
             WindDirection text , WindScale INTEGER ,
             PRIMARY KEY (City)) ''')
cur.execute("INSERT INTO WeatherData(City, WeatherDay) VALUES(?,?)",(city,weatherday))
cur.execute('select * from WeatherData')
print(cur.fetchall())
con.commit()
con.close()
