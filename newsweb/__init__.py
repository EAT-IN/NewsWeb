from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis

from config import config

db = SQLAlchemy()  # 放在外面是方便给manage进行调用


def create_app(config_name):
    app = Flask(__name__)  # 初始化app

    app.config.from_object(config[config_name])  # 加载配置项

    db.init_app(app)  # 实例化数据库对象

    redis_store = StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)  # 实例化redis对象

    CSRFProtect(app)  # 开启csrf防护
    Session(app)  # 实例化session对象

    return app
