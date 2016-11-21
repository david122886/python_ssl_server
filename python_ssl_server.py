from flask import Flask
import sys,os
import json
app = Flask(__name__)


@app.route('/')
def hello_world():
    return json.dumps([{'name':'xiaoLiZi','age':24},{'name':'xiaoWang','age':20},{'name':'zhangShan','age':18}])


if __name__ == '__main__':
    """
    1.crt 和 key文件设置绝对路径才有效,不知道为啥相当路径不行,以后再研究吧,有知道原因的可以一起分享下
    2.host 指向本机ip地址,localhost(127.0.0.1)不取作用,macx ip 地址可以通过终端ifconfig命令获取

    """
    context = (sys.path[0] + '/ssl.cert', sys.path[0] + '/ssl.key')
    app.run(debug=1, host='192.168.1.129', port=5500, ssl_context=context)
