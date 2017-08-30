from flask import Flask,request,render_template,make_response,url_for

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/signin',methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin',methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password =='password':
        return render_template('signin-ok.html',username = username)
    return render_template('form.html',message = 'Bad username or password',username = username)

@app.route('/test',methods=['GET'])
def test():
    return render_template('test.html')

#with app.test_request_context():
#    print(url_for('test'))

@app.route('/test',methods=['POST'])
def test_1():
    username = request.form['user']
    if username =='user':
        return render_template('signin-ok.html',username = username)
    return render_template('test.html')


@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'),404)
    resp.headers['X-something'] = 'A value'
    return resp

if __name__ =='__main__':
    app.run()
