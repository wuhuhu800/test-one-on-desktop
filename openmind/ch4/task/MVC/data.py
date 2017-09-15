import practicetest
import sqlite3
import time


#以下是创建数据表
#cur.execute('''CREATE TABLE WeatherData

#            (City text NOT NULL ,WeatherDay text , WeatherNight text,
#             TemperatureHigh real , TemperatureDailylow real ,
#             WindDirection text , WindScale INTEGER ,
#             PRIMARY KEY (City)) ''')

con = sqlite3.connect('weather.db')
cur = con.cursor()
UserInputCity = input('请输入所要查询的城市>>>')

#以下是传入一个用户输入的城市，为了这句话用：format(', '.join('?' for _ in city)), city
city = [UserInputCity]
#以下是为了做判断空的用的
ListForCompare =[]
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

#以下内容如果查询的城市在数据库里，直接显示
else:
    print(row)

#以下目的是定时更新数据库，每隔3小时更新一次
while True:
    time.sleep(10800)#注意参数是秒
    cur.execute('select City from WeatherData')
    try:
        for Cityi in cur.fetchall():#取出数据库的关键字进行更新
            #Cityi[0]是数据库的城市名称
            WeatherDay1 = practicetest.SearchWeather(Cityi[0])[1]
            WeatherNight1 = practicetest.SearchWeather(Cityi[0])[2]
            TemperatureHigh1 = practicetest.SearchWeather(Cityi[0])[3]
            TemperatureLow1 = practicetest.SearchWeather(Cityi[0])[4]
            WindDirection1 = practicetest.SearchWeather(Cityi[0])[5]
            WindScale1 = practicetest.SearchWeather(Cityi[0])[6]

            cur.execute('UPDATE WeatherData SET \
            WeatherDay = ? ,\
            WeatherNight= ?,\
            TemperatureHigh= ?,\
            TemperatureDailylow= ?,\
            WindDirection= ?,\
            WindScale= ? \
            WHERE City= ?',(WeatherDay1,WeatherNight1,TemperatureHigh1,TemperatureLow1,WindDirection1,WindScale1,Cityi[0]))
            time.sleep(50)#注意参数是秒

    except sqlite3.OperationalError:
        print("database locked!!!")
        con.commit()#每次更新完之后保存
        con.close()






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

'''
#以下目的是定时更新数据库，每隔3小时更新一次,问题是容易锁表。
while True:
    time.sleep(10800)#注意参数是秒
    cur.execute('select City from WeatherData')
    try:
        for Cityi in cur.fetchall():#取出数据库的关键字进行更新
            #Cityi[0]是数据库的城市名称
            WeatherDay1 = practicetest.SearchWeather(Cityi[0])[1]
            WeatherNight1 = practicetest.SearchWeather(Cityi[0])[2]
            TemperatureHigh1 = practicetest.SearchWeather(Cityi[0])[3]
            TemperatureLow1 = practicetest.SearchWeather(Cityi[0])[4]
            WindDirection1 = practicetest.SearchWeather(Cityi[0])[5]
            WindScale1 = practicetest.SearchWeather(Cityi[0])[6]

            cur.execute('UPDATE WeatherData SET WeatherDay = ? WHERE City= ?',(WeatherDay1,Cityi[0]) )
            cur.execute('UPDATE WeatherData SET WeatherNight = ? WHERE City= ?',(WeatherNight1,Cityi[0]) )
            cur.execute('UPDATE WeatherData SET TemperatureHigh = ? WHERE City= ?',(TemperatureHigh1,Cityi[0]) )
            cur.execute('UPDATE WeatherData SET TemperatureDailylow = ? WHERE City= ?',(TemperatureLow1,Cityi[0]) )
            cur.execute('UPDATE WeatherData SET WindDirection = ? WHERE City= ?',(WindDirection1,Cityi[0]) )
            cur.execute('UPDATE WeatherData SET WindScale = ? WHERE City= ?',(WindScale1,Cityi[0]) )

            time.sleep(20)#注意参数是秒

    except sqlite3.OperationalError:
        print("database locked!!!")
    con.commit()#每次更新完之后保存
    con.close()
'''
