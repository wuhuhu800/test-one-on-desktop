'''
服务端运行程序
'''

from flask import Flask,request,render_template,make_response,url_for,session,redirect
import practicetest #导入practicetest.py文件，注意导入文件不能命名XXX2-3，否则报错
import json
from jinja2 import Template
from jinja2 import Environment, PackageLoader
import sqlite3

#import jinja2
#import os.path
#env = jinja2.Environment(
#    loader=jinja2.FileSystemLoader('%s/templates/' % os.path.dirname(__file__))
#)
#env = Environment(loader=PackageLoader('yourapplication', 'templates'))
#template = env.get_template('Weather.html')
historydate ={}


app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.do')#jinja语句中可以用with关键词
app.jinja_env.add_extension('jinja2.ext.loopcontrols')#jinjia语句中可以用do关键词
#@app.route('/login/<name>',methods=['GET'])
#def loginget(name):
#    return render_template('login.html')
'''
@app.before_request
def before_request():
    g.db = sqlite3.connect('logindata.db')

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        name = request.form['user']
        password = request.form['password']
        cursor = g.db.execute('select * from users where name = ? and  password=?',[name,password])
        if cursor.fetchone() is not None:
            session['user']= name
            flash('Login successfully!')
        else:
            flash('No such user!', 'error')
            return redirect(url_for('login'))
    else:
        return render_template('login.html')
    SECRET_KEY = 'secret_key_1'



@app.route('/logout')#以下功能就是让用户登出的功能
def logout():
    session.pop('user',None)#猜想是登出时的操作
    return redirect(url_for('login'))
'''

@app.route('/home')
@app.route('/home/<name>',methods=['GET','POST'])
def home(name=None):
    return render_template('home.html',name = name,digits=[1,2,3,4,5],\
    users=[{'name':'John'},
           {'name':'Tom','hidden':True},
           {'name':'Lisa,'},
           {'name':'Bob'}])


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
    print(1+2)
