from flask import render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash

from apps.cms import cms_bp
from apps.models.UserModel import AdminUser, db
from apps.forms.UserForms import LoginForms, ResetPasswordForm, RegisterForms


# 用户注册
@cms_bp.route('/register/', endpoint='register', methods = ['GET', 'POST'])
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
        print(forms.password.data)
        if u1 and u1.check_password(forms.password.data):
            resp = redirect(url_for('cms.index'))
            resp.set_cookie('id',str(u1.id), path='/')
            return resp
    return render_template('reg_login.html', flags='登录', forms=forms)


# 个人中心
@cms_bp.route('/info/', endpoint='info', methods=['GET', 'POST'])
def InfoView():


    return render_template('reg_login.html')





# 重置密码
@cms_bp.route('/reset/', endpoint='reset', methods=['GET', 'POST'])
def RestPassword():
    forms = ResetPasswordForm(request.form)
    id = request.cookies.get('id')
    if request.method == 'POST' and forms.validate():
        u1 = AdminUser.query.filter_by(id=int(id)).first()
        print(f'原始密码{u1.password}')

        # 更改密码
        u1.password = generate_password_hash(forms.NewPasswd.data)
        db.session.commit()
        print(f'新密码{u1.password}')
        return redirect(url_for('cms.index'))
    return render_template('reg_login.html', flags='修改密码', forms=forms)