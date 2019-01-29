# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis


# 链接数据库之前需要先链接数据库  获取数据库控制对象
class Config(object):
    """配置信息"""
    # 开启DEBUG模式
    DEBUG = True

    # 设置相应的mysql连接方式
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/flask"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    # 配置redis相关参数
    REDIS_HOST = "127.0.0.1"  # redis链接
    REDIS_PORT = 6379  # redis端口


app = Flask(__name__)  # 初始化app

app.config.from_object(Config)  # 加载配置项

db = SQLAlchemy(app)  # 实例化数据库对象

redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)  # 实例化redis对象

CSRFProtect(app)  # 开启csrf防护


@app.route('/')
def index():
    return "index"


if __name__ == '__main__':
    app.run()
