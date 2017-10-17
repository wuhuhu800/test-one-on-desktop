from flask import Flask,render_template,session, redirect, url_for,flash
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_moment import Moment
from datetime import datetime

#*********以下用于表单*************
#from flask_wtf import Form
from flask_wtf import Form
#import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
#******以上用于表单模块************



app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
#初始化对Flask-Bootstrap 输出的 Bootstrap 类初始化，初始化类的目的就是为了给类分配内存空间
moment = Moment(app)

app.config['SECRET_KEY'] = 'hard to guess string'
#为了实现 CSRF 保护，Flask-WTF 需要程序设置一个密钥。Flask-WTF 使用这个密钥生成加密令牌

@app.route('/',methods=['GET', 'POST'])
def index():
#******以下用于表单模块*********
    name = None
    form = NameForm()
    if form.validate_on_submit():
#validate_on_submit()方法会调用表单form中的name字段上附属的Required()验证函数
#如果没有在表单中输入数据，validate_on_submit()方法仍然返回False，从而重复上一步骤。如果表单数据不为空，validate_on_submit()方法就返回True
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        #name = form.name.data

#当validate_on_submit()方法返回True，就执行接下来的if语句。StringField中有一个data属性，可用于获取输入表单中的数据。
#于是这里通过form中的name字段中的data属性获取用户输入表单中的名字，并将其赋值给局部变量name。
        #form.name.data = ''
#赋值完毕后，再将data属性的值设置为空字符串，从而清空表单的name字段
#*******以上用于表单模块*************
        session['name'] = form.name.data
#局部变量 name 被用于存储用户在表单中输入的名字。这个变量现 在保存在用户会话中，即 session['name']
        return redirect(url_for('index'))
#redirect() 是个辅助函数， 用来生成 HTTP 重定向响应
#url_for() 函数的第一个且唯一必须指定的参数是端点名，即路由的内部名字
    return render_template('index.html',current_time=datetime.utcnow(),form=form, name=session.get('name'))

#current_time 是引入moment = Moment(app)
@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

if __name__ == "__main__":
    #manager.run() #manager.run()代替了app.run()，启动后就能解析命令行啦
    app.run(debug = True)
