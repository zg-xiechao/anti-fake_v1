from functools import wraps
from flask import request, redirect, url_for
from apps.models.UserModel import AdminUser,db

# 登录权限验证
def login_request(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        id = request.cookies.get('id', None)
        if id:
            u1 = AdminUser.query.filter_by(id=int(id)).first()
            if u1:
                return fn(*args, **kwargs)
        return redirect(url_for('cms.login'))
    return inner
