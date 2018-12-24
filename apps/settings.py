import os


############################## 开发版 ########################################


# 路径(数据库)
def get_path():
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return path


# 连接到sqlite数据库
class DevBase():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/DevDate.db'.format(get_path())
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# 开发版配置文件  CMS
class DevCMSConfig(DevBase):
    WTF_CSRF_SECRET_KEY = os.urandom(24)