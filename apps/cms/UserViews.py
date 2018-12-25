from flask import render_template, request, redirect, url_for
from apps.cms import cms_bp
from apps.models.UserModels import AdminUser, db
from apps.forms.UserForms import LoginForms, RegisterForms


# 用户注册
@cms_bp.route('/register/', endpoint='register', methods=['GET', 'POST'])
def Register():
    forms = RegisterForms(request.form)
    if request.method == 'POST' and forms.validate():
        s1 = AdminUser()
        s1.set_attrs(forms.data)
        db.session.add(s1)
        db.session.commit()
        return redirect(url_for('cms.login'))
    return render_template('reg_login.html', flags='注册', forms=forms)


# 用户登录
@cms_bp.route('/login/', endpoint='login', methods=['GET', 'POST'])
def Login():
    forms = LoginForms(request.form)
    if request.method == 'POST' and forms.validate():
        u1 = AdminUser.query.filter_by(username=forms.user.data).first()
        if u1 and u1.check_password(password=forms.password.data):
            resp = redirect(url_for('cms.index'))
            resp.set_cookie('id', u1.id, path='/')
            return resp
    return render_template('reg_login.html', flags='登录', forms=forms)


