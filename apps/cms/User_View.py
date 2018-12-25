from flask import render_template, request, redirect, url_for
from apps.cms import cms_bp
from apps.models.UserModel import AdminUser, db
from apps.forms.UserForms import LoginForms


# 用户注册
@cms_bp.route('/register/', endpoint='register', methods = ['GET', 'POST'])
def Register():
    forms = LoginForms(request.form)
    if request.method == 'POST' and forms.validate():
        s1 = AdminUser()
        s1.set_attrs(forms.data)
        db.session.add(s1)
        db.session.commit()
        return redirect(url_for('cms.login'))
    return render_template('reg_login.html', flags='注册', forms=forms)


# 用户登录
@cms_bp.route('/login/', endpoint='login', methods= ['GET', 'POST'])
def Login():
    forms = LoginForms(request.form)
    if request.method == 'POST' and forms.validate():



        return render_template('reg_login.html')