from OneToOne.NO_MAPPING.flask_with_mvc.flask_with_mvc.config import app,db,example
from flask import request,render_template
from OneToOne.NO_MAPPING.flask_with_mvc.flask_with_mvc.models import Address



@app.route("/address/save/",methods=['POST',"GET"])
def add_or_update_address():        #add/update
    msg = ""
    if request.method=='POST':
        formdata = request.form        # as its a post method
        aid = int(formdata.get('adrid'))
        adr = Address.query.filter_by(id=aid).first()

        if adr:

            adr.city = formdata.get('adrcity')
            adr.state = formdata.get('adrstate')
            adr.pincode = formdata.get('adrpin')
            db.session.commit()
            msg = "Address Record Updated..!"
        else:
            #server will add adrid -->
            adr = Address(city=formdata.get('adrcity'),state=formdata.get('adrstate'),pincode=formdata.get('adrpin'))
            db.session.add(adr)
            db.session.commit()
            msg = "Address Record Saved into Database"
    return render_template('address.html',
                           mapping = example,
                           adr = Address.get_dummy_address(),
                           adrlist = Address.query.all(),
                           resp = msg)

@app.route("/address/edit/<int:aid>")   #pathvariable
def fetch_address_for_edit(aid):    #fetch
    return render_template('address.html',
                           mapping=example,
                           adr=Address.query.filter_by(id=aid).first(),
                           adrlist=Address.query.all(),
                           resp='')

@app.route("/address/delete/<int:aid>")   #pathvariable
def delete_address_record(aid): #delete
    msg = ''
    adr = Address.query.filter_by(id=aid).first()
    if adr:
        db.session.delete(adr)
        db.session.commit()
        msg = "Address Record Deleted "
    return render_template('address.html',
                           mapping=example,
                           adr=Address.get_dummy_address(),
                           adrlist=Address.query.all(),
                           resp=msg)



if __name__ == '__main__':
    app.run(debug=True)