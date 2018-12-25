from wtforms import Form, StringField, validators, PasswordField


# 用户注册验证
class RegisterForms(Form):
    user = StringField(
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
            validators.Length(min=16, message='密码长度不能小于16位')
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
            validators.Length(min=16,message='密码不能大于16位')
        ],
        render_kw=({'class': 'form-control', 'placeholder': '请输入密码'})
    )






