from apps.models import BaseModel, db


class TraceModel(BaseModel):
    log_code = db.Column(db.Integer, comment='物流码')
    pro_type = db.Column(db.String(32), comment='产品类别')
    company = db.Column(db.String(32), comment='生产企业')
    pro_date = db.Column(db.DateTime, comment='生产日期')
    is_fake = db.Column(db.Boolean, comment='是否假货,0:假  1:真')
    fake_num = db.Column(db.Integer, comment='防伪数量')
    query_type = db.Column(db.String(32), comment='查询类别')
    query_time = db.Column(db.DateTime, comment='查询时间')
    query_site = db.Column(db.String(128), comment='查询地点')
    query_id = db.Column(db.Integer, comment='查询id')


class FakeModel(BaseModel):
    pro_id = db.Column(db.Integer, comment='产品id')
    arise_time = db.Column(db.DateTime, comment='出现时间')
    arise_site = db.Column(db.String(32), comment='出险地点')
    add_people = db.Column(db.String(8), comment='添加人')


class ProductModel(BaseModel):
    company_id = db.Column(db.Integer, comment='厂家id')
    pro_type = db.Column(db.String(16), comment='产品类型')
    pro_name = db.Column(db.String(16), comment='产品名字')
    pro_stand = db.Column(db.String(32), comment='产品规格')
    pro_date = db.Column(db.DateTime, comment='生产日期')
    exp_date = db.Column(db.DateTime, comment='保质期')
    pro_area = db.Column(db.String(128), comment='产地')
    label = db.Column(db.String(255), comment='防伪标志')
    pro_code = db.Column(db.String(32), comment='产品编号')
    pro_place = db.Column(db.String(255), comment='产地')
    qua_feat = db.Column(db.String(255), comment='质量特色')
    manu_tech = db.Column(db.String(255), comment='生产工艺')
