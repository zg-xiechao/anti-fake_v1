from flask import render_template
from apps.cms import cms_bp



# 首页
@cms_bp.route('/', endpoint='index', methods=['GET', 'post'])
def Index():
    return render_template('index.html')
