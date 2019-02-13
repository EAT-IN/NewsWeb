# -*- coding: utf-8 -*-
from flask_script import Manager
from flask import jsonify, session
from flask_migrate import Migrate, MigrateCommand
from newsweb import create_app, db

app = create_app("development")  # 在创建应用的时候指定配置类

manager = Manager(app)  # 使用Manager进行管理启动app

Migrate(app, db)  # 创建迁移对象
manager.add_command('db', MigrateCommand)  # 把db命令绑定到manager上


@app.route('/')
def index():
    session['user_id'] = '18'
    return jsonify({"name": "ZB", "age": 23})


if __name__ == '__main__':
    manager.run()
