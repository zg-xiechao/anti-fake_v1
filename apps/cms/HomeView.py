from flask import render_template
from apps.cms import cms_bp
from apps.tools.helper import login_request


# 首页
@cms_bp.route('/', endpoint='index', methods=['GET', 'post'])
@login_request
def Index():
    return render_template('index.html')
