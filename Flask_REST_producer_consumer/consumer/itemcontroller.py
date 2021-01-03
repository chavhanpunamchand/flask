from flask import Flask,request,render_template
from Flask_REST_producer_consumer.consumer.iteminfo import Item
from Flask_REST_producer_consumer.consumer.rest_service_consumer import ProductAPIConsumer
app = Flask(__name__)

FILE_PATH = 'D:\\python_work\\flask_projects\\flask_rest_api_end_to_end\\consumer\\photos\\'

@app.route("/product/",methods=["GET","POST"])
def add_or_updateproduct():
    msg = ''
    if request.method == 'POST':
        reqdata  = request.form         # form data

        file = request.files['itph']
        file.save(FILE_PATH+reqdata.get('itnm')+".png")       # consume machine vr...

        itmid = reqdata.get('itid')
        prod = ProductAPIConsumer.get_product(itmid)
        itm = Item(itid=itmid,
             itnm=reqdata.get('itnm'),
             itqty=reqdata.get('itqt'),
             itpr=reqdata.get('itpr'),
             itpht='NA')
        if type(prod)==Item:
            msg = ProductAPIConsumer.update_product(itmid,itm)
        else:
            msg = ProductAPIConsumer.add_product(itm)
    return render_template('product.html',resp = msg,itemlist = ProductAPIConsumer.get_all_products(),item = Item.get_dummy())

@app.route('/product/edit/<int:itid>',methods=['GET'])
def get_item_info(itid):
    return render_template('product.html',resp = '',
                           itemlist = ProductAPIConsumer.get_all_products(),
                           item = ProductAPIConsumer.get_product(itid))

@app.route('/product/delete/<int:itid>',methods=['GET'])
def delete_item_record(itid):
    msg = ProductAPIConsumer.delete_product(itid)
    return render_template('product.html', resp=msg,
                           itemlist=ProductAPIConsumer.get_all_products(),
                           item=Item.get_dummy())


if __name__ == '__main__':
    app.run(debug=True,port=5001)
