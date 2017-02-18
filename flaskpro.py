#coding:utf8
from flask import Flask
from flask import render_template,redirect,url_for
import flask

app = Flask(__name__)
app.debug = True


@app.route('/login/',methods=['POST','GET'])
def login():
    #设置错误标志位为None
    error = None
    #如果模式为POST
    if flask.request.method == 'POST':
        #加上名字判断,如果与输入名字相等，则返回新的URL否则报错。
        #if flask.request.form['username']:
        #返回你输入的名字重定向到url中
        return redirect(url_for('index',username=flask.request.form['username'],password=flask.request.form['password']))
        #else:
         #   error = 'Invalid username/password'
    #不是POST模式，则返回模版
    return render_template('login.html',error=error)

#入口
@app.route('/')
def index():
    return render_template('index.html',username=flask.request.args.get('username'),password=flask.request.args.get('password'))



if __name__ == '__main__':
    app.run()
