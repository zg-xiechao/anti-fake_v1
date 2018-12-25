from flask import Blueprint

cms_bp = Blueprint('cms', __name__)

# 导入子模块
from apps.cms import *
