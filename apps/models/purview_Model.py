from apps.models import db, BaseModel


# 管理员信息表
class AdminUser(BaseModel):
    username = db.Column(db.String(16), unique=True, comment='用户名')

    password = db.Column(db.String(128), comment='密码')

    name = db.Column(db.String(8), comment='管理员姓名')

    tel = db.Column(db.String(12), unique=True, comment='电话号码')

    email = db.Column(db.String(32), unique=True, comment='邮箱账号')