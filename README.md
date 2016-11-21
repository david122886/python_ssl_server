# python_ssl_server
一个简单搭建支持https  python web服务器和简单IOS端https实现


##坑：
1.项目名不能和系统默认模块或者第三方模块名相同，不然无法找到正确模块（AttributeError: module 'ssl' has no attribute 'PROTOCOL_SSLv23’）
