from apps.models import db, BaseModel


# 企业信息表
class Merchant(BaseModel):
    username = db.Column(db.String(16), unique=True, comment='商家用户名')

    password = db.Column(db.String(128), comment='商家密码')

    company = db.Column(db.String(32), comment='企业名称')

    name = db.Column(db.String(4), comment='法人姓名')

    tel = db.Column(db.String(12), unique=True, comment='电话号码')

    email = db.Column(db.String(21), unique=True, comment='邮箱账号')

    register_add = db.Column(db.String(128), comment='注册地址')

    longitude = db.Column(db.String(255), comment='商家经度')

    latitude = db.Column(db.String(255), comment='商家纬度')

    status = db.Column(db.Integer, comment='状态  0:提交,待审核  1:审核通过  2:审核拒绝')

    end_time = db.Column(db.DateTime, comment='营业执照到期时间')

    company_papers = db.Column(db.String(128), comment='企业证件,七牛云地址')

    company_type = db.Column(db.String(8), comment='企业类型')
