from flask import request
from wtforms import Form, StringField, validators, PasswordField
from apps.models.UserModel import AdminUser



# 用户注册验证
class RegisterForms(Form):
    username = StringField(
        validators=[
            validators.DataRequired(message='用户名不能为空!'),
            validators.Length(min=3, message='用户名不能小于3个字符'),
            validators.Length(max=8, message='用户名不能大于8个字符')
        ],
        render_kw=({'class': 'form-control', 'placeholder': '请填写用户名!'})
    )


    password = PasswordField(
        validators=[
            validators.DataRequired(message='密码不能为空'),
            validators.Length(min=6, message='密码长度不能小于6位'),
            validators.Length(max=16, message='密码长度不能小于16位')
        ],
        render_kw=({'class': 'form-control', 'placeholder': '请输入密码!'})
    )


    repassword = PasswordField(
        validators=[
          validators.DataRequired(message='重复密码不能为空'),
          validators.EqualTo('password', message='再次密码不一样')
        ],
    render_kw=({'class':'form-control', 'placeholder':'再次输入密码!'})
    )



    tel = StringField(
        validators=[
            validators.DataRequired(message='手机号码不能为空'),
            validators.Regexp(r'^((13[0-9])|(14[5,7])|(15[0-3,5-9])|(17[0,3,5-8])|(18['
                              r'0-9])|166|198|199)\d{8}$', message="请输入正确的电话号码"),
        ],
        render_kw=({'class': 'form-control', 'placeholder': '请输入手机号码!'})
    )


    # 自定义字段验证
    def validate_tel(self, obj):
        tel = obj.data
        phone = AdminUser.query.filter_by(tel=tel).first()
        if phone:
            raise validators.ValidationError('手机号码已存在!')

    def validate_username(self, obj):
        user = obj.data
        u1 = AdminUser.query.filter_by(username=user).first()
        if u1:
            raise validators.ValidationError('此用户名已存在!')






# 用户登录验证
class LoginForms(Form):
    user = StringField(
        validators=[
            validators.DataRequired(message='帐号不能为空'),
            validators.Length(min=3, message='用户名不能小于3位'),
            validators.Length(max=8, message='用户名不能大于8位')
        ],
        render_kw=({'class': 'form-control', 'placeholder': '请输入用户名'})
    )


    password = PasswordField(
        validators=[
            validators.DataRequired(message='密码不能为空'),
            validators.Length(min=6,message='密码不能小于6位'),
            validators.Length(max=16,message='密码不能大于16位')
        ],
        render_kw=({'class': 'form-control', 'placeholder': '请输入密码'})
    )



# 重置密码
class ResetPasswordForm(Form):
    oldpass = PasswordField(
        validators=[
            validators.DataRequired(message='旧密码不能为空'),
            validators.Length(min=6, message='密码长度不能小于6位'),
            validators.Length(max=16, message='密码长度不能大于16位')
        ],
        render_kw=({'class': 'form-control', 'placeholder': '请输入密码'})
    )

    NewPasswd = PasswordField(
        validators=[
            validators.DataRequired(message='新密码不能为空!'),
            validators.Length(min=6, message='密码长度不能小于6位'),
            validators.Length(max=16, message='密码长度不能大于16位')
        ],
        render_kw=({'class': 'form-control', 'placeholder': '请输入新密码'})
    )


    # 自定义字段验证
    def validate_oldpass(self, obj):
        pwd = obj.data
        id = request.cookies.get('id', None)
        u1 = AdminUser.query.filter_by(id=id).first()
        if not id and not u1.check_password(pwd):
            raise validators.ValidationError('密码不正确!')





