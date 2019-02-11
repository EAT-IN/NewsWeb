# -*- coding: utf-8 -*-
class Config(object):
    """配置信息"""
    DEBUG = 1  # 开启DEBUG模式
    ENV = "development"  # 开启开发模式

    # 设置相应的mysql连接方式
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:mysql@127.0.0.1:3306/flask"  # 连接数据库,使用pymysql需要+pymysql
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 动态追踪修改设置，如未设置只会提示警告
    SQLALCHEMY_ECHO = True  # 显示转换后的原生sql语句

    # 配置redis相关参数
    REDIS_HOST = "127.0.0.1"  # redis链接
    REDIS_PORT = 6379  # redis端口
