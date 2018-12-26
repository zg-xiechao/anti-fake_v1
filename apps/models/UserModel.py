from apps.models import db, BaseModel
from werkzeug.security import check_password_hash, generate_password_hash


# 管理员信息表
class AdminUser(BaseModel):
	username = db.Column(db.String(16), unique=True, comment='用户名')

	_password = db.Column('password', db.String(128), comment='密码')

	name = db.Column(db.String(8), comment='管理员姓名')

	tel = db.Column(db.String(12), unique=True, comment='电话号码')

	email = db.Column(db.String(32), unique=True, comment='邮箱账号')

	@property
	def password(self):
		return self._password

	@password.setter
	def password(self, value):
		self._password = generate_password_hash(value)


	# 校对密码
	def check_password(self, raw_passwrod):
		return check_password_hash(self._password, raw_passwrod)


	def __repr__(self):
		return "<AdminUser {}>".format(self.username)
