from flask import Flask
import sys,os
import json
app = Flask(__name__)


@app.route('/')
def hello_world():
    return json.dumps([{'name':'xiaoLiZi','age':24},{'name':'xiaoWang','age':20},{'name':'zhangShan','age':18}])


if __name__ == '__main__':
    context = (sys.path[0] + '/ssl.cert', sys.path[0] + '/ssl.key')
    app.run(debug=1, host='192.168.1.129', port=5500, ssl_context=context)
