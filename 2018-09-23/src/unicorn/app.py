#!/usr/bin/env python
# -*- encoding:utf8 -*-

from flask import Flask
import mysql.connector

app = Flask(__name__)
conn = mysql.connector.connect(host = 'mysql', port = 3306, user = 'unicorn', database = 'hoge', password = 'unicorn')

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/db/get')
def get():
    cur = conn.cursor()
    cur.execute('SELECT * FROM fuga')
    return cur.fetchall()[-1][0]

@app.route('/db/put/<query>')
def put(query):
    cur = conn.cursor()
    try:
        cur.execute('INSERT INTO fuga (col) VALUES (%s)', [query])
        conn.commit()
        return '%s inserted!' % query
    except:
        conn.rollback()
        return 'insertion failed.'

if __name__ == '__main__':
    app.run(host='unicorn', debug=True, port=8000)
