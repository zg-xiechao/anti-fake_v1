from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


# 基类
class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, comment='主键ID')

    isDelete = db.Column(db.Integer, default=0, comment='是否删除')

    add_time = db.Column(db.DateTime, default=datetime.now(), comment='添加时间')



# 导入子 Model
from apps.models import purview_Model
from apps.models import Merchant_Model




