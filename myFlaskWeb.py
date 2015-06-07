__author__ = 'Lv_Sage'
# -*- coding: utf-8 -*-

from flask import Flask
#from flask import request
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask import render_template

app = Flask(__name__)

manage = Manager(app)
bootstrap = Bootstrap(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def index():
    return render_template('index.html')
    #user_agent = request.headers.get('User-Agent')
    #return '<p>Your browser is %s</p>' % user_agent
    #return '<h1>错误的请求哟！</h1>',400


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
    #return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)
    #manager.run()
