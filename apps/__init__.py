from flask import Flask
from flask_session import Session




# 数据库
def register_db(app: Flask):
    from apps.models import db
    db.init_app(app=app)


# 蓝图
def register_cms_bp(app: Flask):
    from apps.cms import cms_bp
    app.register_blueprint(cms_bp)


# 创建app
def create_app(config: str):
    app = Flask(__name__, static_url_path='/static/', static_folder='./static')
    app.config.from_object(config)

    # session
    Session(app=app)

    # 数据库
    register_db(app=app)

    # 蓝图
    register_cms_bp(app=app)

    return app