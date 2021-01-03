from flask import Flask,request,render_template
from Flask_end_to_end.configurations.app_config import app
from Flask_end_to_end.models.productinfo import Product
from Flask_end_to_end.dao.productdaoimp import ProductDAOORMImpl
dbop=ProductDAOORMImpl()


@app.route('/index/',methods=['GET'])
def welcome_page():
    return render_template('product.html',prodlist=dbop.get_all_product(),prod=Product.get_dummy_product())

@app.route('/persist/',methods=['POST'])
def add_update_product_info():
    formdata=request.form
    pid=int(formdata.get('pid'))
    if pid>0:
        dbpr=dbop.get_product(pid)

    pr=Product(pid=formdata.get('pid'),
             name =formdata.get('pname'),
             qty = formdata.get('pqty'),
             price = formdata.get('pprice'),
             cat = formdata.get('pcat'),
             vendor= formdata.get('pvendor'))
    msg=dbop.add_product(pr)
    return render_template('product.html',resp=msg,prodlist=dbop.get_all_product(),prod=Product.get_dummy_product())


@app.route('/edit/<int:pid>',methods=['GET'])
def edit_product_info(pid):
    return render_template('product.html',prodlist=dbop.get_all_product(),prod=dbop.get_product(pid))


@app.route('/delete/<int:pid>',methods=['GET'])
def delete_product_info(pid):
    msg=dbop.delete_product(pid)
    return render_template('product.html',prodlist=dbop.get_all_product(),prod=Product.get_dummy_product(),resp=msg)

