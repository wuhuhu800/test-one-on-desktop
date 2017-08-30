from flask import Flask,request,render_template,make_response,url_for
import practicetest

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/signin',methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin',methods=['POST'])
def signin():
#以下一行将request.form[username]输入的内容作为参数传给天SearchWeather的参数，再给username
    username = practicetest.SearchWeather(request.form['username'])
    return render_template('form.html',message = username)

#    password = request.form['password']


#    if username == 'admin'  and password =='password':
#        return render_template('signin-ok.html',username = username)
#    return render_template('form.html',message = 'Bad username or password',username = username,password = password)

@app.route('/test',methods=['GET'])
def test():
    return render_template('test.html')

#with app.test_request_context():
#    print(url_for('test'))

@app.route('/test',methods=['POST'])
def test_1():
    username = practicetest.SearchWeather(request.form['user'])

#    username = request.form["user"]#form就是test.html里的form，form里的user参数就是test.html里的form的input的name的值,request.form
#    helpdoc = request.form['help']
#    if username =='user':
#        return render_template('signin-ok.html',username = username)#此处黄色username应该是模板里的{{username}}，白色username是变量
#    elif helpdoc == 'POST':
#        return render_template('home.html')
#    else:
#        print(1)

    return render_template('test.html',message = username)


@app.errorhandler(404) #404报错
def not_found(error):
    resp = make_response(render_template('error.html'),404)
    resp.headers['X-something'] = 'A value'
    return resp


@app.route('/student')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
   return render_template("result.html",result = result)
'''
@app.route('/newtest',methods=['GET'])
def newtest_form():
    return render_template('newtest.html')

@app.route('/newtest',methods=['POST'])
def newtest():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password =='password':
        return render_template('signin-ok.html',username = username)
    return render_template('form.html',message = 'Bad username or password',username = username)

@app.route('/signin',methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin',methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password =='password':
        return render_template('signin-ok.html',username = username)
    return render_template('form.html',message = 'Bad username or password',username = username,password = password)

'''



if __name__ =='__main__':
    app.run()
