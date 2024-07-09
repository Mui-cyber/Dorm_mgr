from user_conf import WEB_LISTEN_PORT, WEB_LISTEN_IP
from flask import Flask

from .frontend import frontend_blueprint
from .backend import backend_blueprint

__all__ = ["run_daemon"]

def run_daemon():
    # 打开Flask
    app = Flask(__name__)

    # 注册蓝图
    app.register_blueprint(frontend_blueprint)
    app.register_blueprint(backend_blueprint)

    app.run(host=WEB_LISTEN_IP,port=WEB_LISTEN_PORT)

print("成功加载前端模块")
