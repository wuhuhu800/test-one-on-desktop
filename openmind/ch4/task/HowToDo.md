用户查询的时候，判断：如果数据库里有值，那么取数据库的；如果数据库没有值，调取接口。并且将接口的数据保存到本地数据库。
点击更正的时候：判断城市是否有值，有，改；如果数据库没有改城市，那么就返回错误值；后面在加上限定条件。


```JavaScript
{'results':
   [
     {
       'location':
        {'id': 'WX4FBXXFKE4F', 'name': '北京', 'country': 'CN', 'path': '北京,北京,中国', 'timezone': 'Asia/Shanghai', 'timezone_offset': '+08:00'},
       'daily':
       [
       {'date': '2017-09-14', 'text_day': '阴', 'code_day': '9', 'text_night': '阴', 'code_night': '9', 'high': '28', 'low': '20', 'precip': '', 'wind_direction': '南', 'wind_direction_degree': '180', 'wind_speed': '10', 'wind_scale': '2'},
       {'date': '2017-09-15', 'text_day': '阴', 'code_day': '9', 'text_night': '阴', 'code_night': '9', 'high': '28', 'low': '18', 'precip': '', 'wind_direction': '南', 'wind_direction_degree': '180', 'wind_speed': '10', 'wind_scale': '2'},
       {'date': '2017-09-16', 'text_day': '阵雨', 'code_day': '10', 'text_night': '阴', 'code_night': '9', 'high': '26', 'low': '18', 'precip': '', 'wind_direction': '南', 'wind_direction_degree': '180', 'wind_speed': '10', 'wind_scale': '2'}],
       'last_update':
       '2017-09-14T08:00:00+08:00'
       }
      ]
     }
  ```
