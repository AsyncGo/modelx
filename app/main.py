from flask import Flask
from config import config

def create_app(env = 'dev'):
    app = Flask(__name__)

    # 注册蓝图
    from .web.controllers import index
    from .web.controllers import execute
    app.register_blueprint(index.index, url_prefix='/index')
    app.register_blueprint(execute.execute, url_prefix='/execute')

    # 附加路由和自定义的错误页面

    return app