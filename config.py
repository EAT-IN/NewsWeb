# -*- coding: utf-8 -*-
import redis


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

    # 定义session密钥
    SECRET_KEY = "xmzhang"

    # flask_session的配置信息
    SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中
    SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 使用 redis 的实例
    PERMANENT_SESSION_LIFETIME = 86400  # session 的有效期，单位是秒
