# -*- coding: utf-8 -*-
'''
Created on 2015年4月29日

@author: dilo
'''

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()