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

  @AIHackers/py101stu-004 阿虎完成 ch5任务啦

- 任务成果地址：[***天气查询地址***]()
- 任务成果截图:
- 个人教程：
这几天主要折腾环境变量，我用的是Anaconda环境，无法直接安装heroku的文档进行，所以还在研究Conda Buildpack安装，安装这个有需要安装conda-requirement.txt, 但直接用”conda install --yes --file requirements.txt“命令提示没有requirement.txt,，google各种搜索，然后发现没有mesa包，
然后下载安装后，还是有问题。最后继续搜，终于在各种尝试下，找到后面的解决方案，用[***conda安装pipenv环境***](https://github.com/ContinuumIO/anaconda-issues/issues/1429)的方案：“$ conda create -n pipenv numpy pip”这条命令，以及用命令行解决 pipenv check报错的“ERROR: The executable xxx2/bin/python3 is not functioning”的[***答案***](https://github.com/pypa/virtualenv/issues/788)所需要的命令“conda install -c anaconda virtualenv=15.1.0”，然后就可以很正常的使用虚拟环境了。下一步就连接数据库，在输入数据库的一步需要输入命令：heroku pg:psql，报错：The local psql command could not be located. For help installing psql, see，各种找，貌似这个问题不是很难，所以回答的人不多，终于在一处翻到了，设置路径：export PATH="/Applications/Postgres.app/Contents/Versions/9.6/bin:$PATH"，这个路径是“/Applications/Postgres.app/Contents/Versions/9.6/bin”是Postgres安装地址，一打开软件就能看到。这下才把官方文档例子跑通。后来在套模板的时候，才发现官方是Dango框架，我用的是flask模型，这不好套啊。关键的时候犹如神助，找到一篇blog，非常简洁完成任务见[***此人blog***](https://progblog.io/How-to-deploy-a-Flask-App-to-Heroku)
- 感想：
还是要坚持的，虽然道路艰难，这次在遇到环境变量的问题的几次崩溃，到了发呆的地步，休息一下，整理可以解决的线索，google，如同大妈说的：一定要对google有信心，你遇到的问题，别人肯定也遇到过。也许就是这个信念，让我没有放弃，不断梳理自己问题线索，寻找答案，尝试答案，整理结果。折腾到最后还是胜利了。每一次的挑战，都会加强自己的信心。发现开智这种学习模式，非常棒，最近体会非常深的就是这种学习模式可以不断训练我们适应陌生，适应挑战，而且更重要的是有信心面对挑战，这是仅仅报个培训班无法解决的，而现实生活中仅仅是解决知识层面的问题用处非常局限，更重要的是解决问题的能力和信心。
