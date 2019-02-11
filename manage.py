# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis
from config import Config

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
