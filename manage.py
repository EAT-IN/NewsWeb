# -*- coding: utf-8 -*-
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from newsweb import app, db

manager = Manager(app)  # 使用Manager进行管理启动app

Migrate(app, db)  # 创建迁移对象
manager.add_command('db', MigrateCommand)  # 把db命令绑定到manager上


@app.route('/')
def index():
    return "index"


if __name__ == '__main__':
    manager.run()
