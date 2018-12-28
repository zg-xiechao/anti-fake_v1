from flask import render_template, request, redirect, url_for
from apps.cms import cms_bp
from apps.models.UserModel import AdminUser, db
from apps.forms.UserForms import LoginForms
from apps.models.TraceModel import ProductModel


@cms_bp.route('/Trace/', endpoint='Trace', methods=['GET', 'POST'])
def trace():
    if request.method == 'GET':
        u1 = ProductModel.query.filter(ProductModel.isDelete == 0).all()
        return render_template('fake.html', form=u1)


@cms_bp.route('/sdypro/',endpoint='sdypro',methods=['GET','POST'])
def sdypro():
    return render_template('sdypro.html')