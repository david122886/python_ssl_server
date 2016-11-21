# python_ssl_server
一个简单搭建支持https  python web服务器和简单IOS端https实现,使用mac系统开发，pythonIDE使用Pycharm,python3.5
##步骤：
1. pip --version  

   查看pip版本最好使用最新的，我用pip 9.0.1
2. python setup.py install --record files.txt
   如果没有安装，https://pypi.python.org/pypi/pip下载安装
3. pip install --upgrade pip
   如果版本比较低，使用此命令更新
4. pip list
   查看安装第三方module，确保有以下库：
   Flask (0.11.1)
   Jinja2 (2.8)
   setuptools (18.2)
   Werkzeug (0.11.11)（重要）
5. python3 -m pip install Werkzeug
  如果没有上面库，安装这些库
6. pip install --upgrade Werkzeug
  如果已经安装但是版本比较低，使用命令更新

##坑：
1.项目名不能和系统默认模块或者第三方模块名相同，不然无法找到正确模块（AttributeError: module 'ssl' has no attribute 'PROTOCOL_SSLv23’）

2.自己创建SSL证书（没有通过CA机构申请）测试站点时Google浏览器无法打开https链接，需换用Safari浏览器
