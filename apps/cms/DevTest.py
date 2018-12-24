from apps.cms import cms_bp
from flask import render_template


@cms_bp.route('/', endpoint='index')
def IndexView():
    return render_template('index.html')