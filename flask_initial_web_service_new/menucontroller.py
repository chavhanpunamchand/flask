from flask_initial_web_service_new.model import *
from flask import Flask,request,render_template,session


@app.route('/menus/',methods=['GET','POST'])
def save_or_update_menus():

    if 'userinfo' in session:


        hotel = Hotel.query.all()

#if user:
        msg  = ''

        if request.method == 'POST':
            id = int(request.form['mid'])
            name = request.form['mname']
            price= request.form['mprice']
            hotelid= request.form['mhotelid']
            dbmenu = Menu.query.filter_by(id=id).first()
            if dbmenu:
                dbmenu.name= name
                dbmenu.price = price
                dbmenu.hotelid = hotelid
                db.session.commit()
                msg = "menu Info Updated Successfully..!"
            else:
                dbmenu = Menu(id=id,name=name,price=price,hotelid=hotelid)
                db.session.add(dbmenu)
                db.session.commit()
                msg = "menu Info Created Successfully...!"

        return render_template('menus.html',
                               resp = msg,user=session['userinfo'],
                               menu = Menu.dummy_menu(),
                               menulist = Menu.query.all()
                               ,hotellist=Hotel.query.all())
    return render_template('login.html', resp='')

@app.route('/menus/edit/<int:mid>')
def edit_menu_info(mid):
    hotel = Hotel.query.all()
    if 'userinfo' in session:
        return render_template('menus.html',
                               resp='',user=session['userinfo'],
                               menu=Menu.query.filter_by(id=mid).first(),
                               menulist=Menu.query.all())
    return render_template('login.html', resp='')

@app.route('/menus/delete/<int:mid>')
def delete_menu_info(mid):
    hotel = Hotel.query.all()
    if 'userinfo' in session:
        msg = ''
        menu = Menu.query.filter_by(id=mid).first()
        if menu:
            db.session.delete(menu)
            db.session.commit()
            msg = "menu Removed Successfully..!"
        return render_template('menus.html',user=session['userinfo'],
                               resp=msg,
                               menu=Menu.dummy_menu(),
                               menulist=Menu.query.all(),
                               hotels=hotel)
    return render_template('login.html', resp='')

FLAG = True

@app.route('/menus/<val>',methods=['GET'])
def toggle_menu_type(val):
    if 'userinfo' in session:
        global FLAG
        allmenus = Menu.query.all()
        if FLAG:
            if val == 'rid':
                allmenus.sort(key=lambda menu : menu.id,reverse =True)
            elif val == 'rtype':
                allmenus.sort(key=lambda menu : menu.type)
            elif val == 'rcharge':
                allmenus.sort(key=lambda menu: menu.charge)
            elif val == 'rstatus':
                allmenus.sort(key=lambda menu: menu.status)
            FLAG = False
        else:
            FLAG = True
        return render_template('menus.html',user=session['userinfo'],
                               resp='',
                               menu=allmenus,
                               menulist=allmenus)
    return render_template('login.html', resp='')

if __name__ == '__main__':
    app.run(debug=True)