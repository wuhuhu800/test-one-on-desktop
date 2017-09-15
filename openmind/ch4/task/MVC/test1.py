import practicetest
#print(practicetest.SearchWeather('北京')[2])
import sqlite3
import time
#i = 0
#while True:
#    time.sleep(10)
#    print(i)
#    i = i +1
con = sqlite3.connect('weather.db')
cur = con.cursor()
cur.execute('select * from WeatherData')
print(cur.fetchall())
con.commit()
con.close()
