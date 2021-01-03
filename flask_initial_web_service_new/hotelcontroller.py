from flask_initial_web_service_new.model import *
from flask import Flask,request,render_template,session

@app.route('/hotel/',methods=['GET','POST'])
def save_or_update_hotels():
    if 'userinfo' in session:
        msg  = ''
        if request.method == 'POST':
            hotel_id = int(request.form['hid'])
            hotel_name = request.form['hname']
            hotel_contact = request.form['hcontact']
            hotel_address = request.form['haddress']
            hotel_website = request.form['hwebsite']
            hotel_accountid = int(request.form['haccid'])
            dbhotel = Hotel.query.filter_by(id=hotel_id).first()
            print(dbhotel)
            if dbhotel:
                dbhotel.name = hotel_name
                dbhotel.contact = hotel_contact
                dbhotel.address = hotel_address
                dbhotel.website = hotel_website
                dbhotel.accno = hotel_accountid
                db.session.commit()
                msg = "Hotel Updated Successfully..!"#hotel_id | hotel_name | hotel_address | hotel_contact | hotel_website  | acc_id
            else:
                dbhotel = Hotel(id=hotel_id,name=hotel_name,address=hotel_address,contact=hotel_contact,website=hotel_website,accno=hotel_accountid)
                db.session.add(dbhotel)
                db.session.commit()
                msg = "Hotel Created Successfully...!"

        return render_template('hotel.html',
                               resp = msg,user=session['userinfo'],
                               hotel = Hotel.dummy_hotel(),
                               hotellist = Hotel.query.all())
    return render_template('login.html', resp='')
@app.route('/hotel/edit/<int:hid>')
def edit_hotel_info(hid):
    if 'userinfo' in session:
        return render_template('hotel.html',
                               resp='',user=session['userinfo'],
                               hotel=Hotel.query.filter_by(id=hid).first(),
                               hotellist=Hotel.query.all())
    return render_template('hotel.html', resp='')
@app.route('/hotel/delete/<int:hid>')
def delete_hotel_info(hid):
    if 'userinfo' in session:
        msg = ''
        hotel = Hotel.query.filter_by(id=hid).first()
        if hotel:
            db.session.delete(hotel)
            db.session.commit()
            msg = "Hotel Removed Successfully..!"
        return render_template('hotel.html',
                               resp=msg,user=session['userinfo'],
                               hotel=Hotel.dummy_hotel(),
                               hotellist=Hotel.query.all())
    return render_template('hotel.html', resp='')
