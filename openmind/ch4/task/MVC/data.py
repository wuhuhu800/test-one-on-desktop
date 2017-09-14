import practicetest
import sqlite3
con = sqlite3.connect('weather.db')
cur = con.cursor()
UserInputCity = input('请输入所要查询的城市>>>')
city = [UserInputCity]#传入一个用户输入的城市，为了这句话用：format(', '.join('?' for _ in city)), city
#

ListForCompare =[]
weatherday = '多云'
cur.execute('SELECT * FROM WeatherData WHERE City in ({0})'.format(', '.join('?' for _ in city)), city)
# 上面这句查询语句作用就是能把一横行的数据都查出来
row = cur.fetchall()
#    以下if完成两件事情
#    1、调用接口查数据
#    2、查到数据保存在数据库里。
if row == ListForCompare:#如果数据库里没有查询的城市的情况
    print(1)
    #以下是调用practicetest的函数SearchWeather的返回值
    WeatherDayDaily = practicetest.SearchWeather(UserInputCity)[1]
    WeatherNightDaily = practicetest.SearchWeather(UserInputCity)[2]
    TemperatureHighDaily = practicetest.SearchWeather(UserInputCity)[3]
    TemperatureLowDaily = practicetest.SearchWeather(UserInputCity)[4]
    WindDirectionDaily = practicetest.SearchWeather(UserInputCity)[5]
    WindScaleDaily = practicetest.SearchWeather(UserInputCity)[6]
    #以下是将函数返回值插入数据库
    cur.execute(
    "INSERT INTO WeatherData(City, WeatherDay,WeatherNight,TemperatureHigh,TemperatureDailylow,WindDirection,WindScale)\
     VALUES(?,?,?,?,?,?,?)",\
     (UserInputCity,WeatherDayDaily,WeatherNightDaily,TemperatureHighDaily,TemperatureLowDaily,WindDirectionDaily,WindScaleDaily))
    cur.execute('SELECT * FROM WeatherData WHERE City in ({0})'.format(', '.join('?' for _ in city)), city)
    row1 = cur.fetchall()
    print(row1)

else:#如果查询的城市在数据库里，直接显示
    print(row)


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
