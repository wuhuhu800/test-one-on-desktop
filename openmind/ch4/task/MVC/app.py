'''
服务端运行程序
'''

from flask import Flask,request,render_template,make_response,url_for
import practicetest #导入practicetest.py文件，注意导入文件不能命名XXX2-3，否则报错
import json
import datas
#from jinja2 import Template
#from jinja2 import Environment, PackageLoader

#env = Environment(loader=PackageLoader('yourapplication', 'templates'))
#template = env.get_template('Weather.html')





app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/Weather',methods=['GET'])
def WeatherGet():
    return render_template('Weather.html')

@app.route('/Weather',methods=['POST'])
def WeatherPost():
    weather = None
    city = None
    historydate = None
    userupd = None
    get_update = None
    historydate ={}
    if request.form['action'] == u'查询':
        city = request.form['city']
        weather = datas.serch_weather_db(city)
        historydate[city]= weather #历史数据列表
    elif request.form['action'] == u'更正':
        city = request.form['city']
        get_update = 1
    return render_template(
    'Weather.html',
    weather = weather,
    city = city,
    historydate=json.dumps(historydate),
    userupd = json.dumps(city),
    get_update = get_update)

@app.errorhandler(404) #404报错
def not_found(error):
    resp = make_response(render_template('error.html'),404)
    resp.headers['X-something'] = 'A value'
    return resp


if __name__ =='__main__':

    app.run(debug = True)
