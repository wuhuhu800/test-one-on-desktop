'''
服务端运行程序
'''

from flask import Flask,request,render_template,make_response,url_for
import practicetest #导入practicetest.py文件，注意导入文件不能命名XXX2-3，否则报错
import json
#from jinja2 import Template
#from jinja2 import Environment, PackageLoader

#env = Environment(loader=PackageLoader('yourapplication', 'templates'))
#template = env.get_template('Weather.html')
historydate ={}

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

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

    app.run()
