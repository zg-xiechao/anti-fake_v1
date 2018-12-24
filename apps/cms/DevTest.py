from apps.cms import cms_bp
from flask import render_template


@cms_bp.route('/', endpoint='index')
def IndexView():
    return render_template('add_cls.html')


@cms_bp.route('/login/', endpoint='login')
def login():
    return render_template('login.html')
