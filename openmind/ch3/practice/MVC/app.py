'''
服务端运行程序
'''

from flask import Flask,request,render_template,make_response,url_for,session,redirect
import practicetest #导入practicetest.py文件，注意导入文件不能命名XXX2-3，否则报错
import json
from jinja2 import Template
from jinja2 import Environment, PackageLoader
#import jinja2
#import os.path
#env = jinja2.Environment(
#    loader=jinja2.FileSystemLoader('%s/templates/' % os.path.dirname(__file__))
#)
#env = Environment(loader=PackageLoader('yourapplication', 'templates'))
#template = env.get_template('Weather.html')
historydate ={}

app = Flask(__name__)
#@app.route('/login/<name>',methods=['GET'])
#def loginget(name):
#    return render_template('login.html')


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['user'] =='admin':
            session['user'] = request.form['user']
            return "Admin login successfully "
        else:
            return 'No such user!'
    if 'user' in session: #登录之后的状态，session已经保存了登录的信息
       return 'Hello %s!' % session['user']
    else:

        title = request.args.get('title','Default')
        return render_template('login.html' , title = title)
app.secret_key='123456'

@app.route('/logout')#以下功能就是让用户登出的功能
def logout():
    session.pop('user',None)#猜想是登出时的操作
    return redirect(url_for('login'))



@app.route('/home/<name>',methods=['GET','POST'])
def home(name):
    return render_template('home.html',name = name )


@app.route('/Weather',methods=['GET'])
def WeatherGet():
    return render_template('Weather.html')

@app.route('/Weather',methods=['POST'])
def WeatherPost():
    user = request.form['user']
    username = practicetest.SearchWeather(user)
    historydate[user]= username #历史数据列表
    return render_template('Weather.html',message = username,user = user,historydate=json.dumps(historydate))

@app.errorhandler(404) #404报错
def not_found(error):
    resp = make_response(render_template('error.html'),404)
    resp.headers['X-something'] = 'A value'
    return resp


if __name__ =='__main__':

    app.run( debug = True)
