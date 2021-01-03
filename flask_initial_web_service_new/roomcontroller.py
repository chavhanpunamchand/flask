from flask_initial_web_service_new.model import *
from flask import Flask,request,render_template,session


@app.route('/rooms/',methods=['GET','POST'])
def save_or_update_rooms():
    if 'userinfo' in session:
   #if user:
        msg  = ''
        if request.method == 'POST':
            rid = int(request.form['rid'])
            type = request.form['rtype']
            charge = request.form['rcharge']
            status = request.form['rstatus']
            dbroom = Room.query.filter_by(id=rid).first()
            if dbroom:
                dbroom.type = type
                dbroom.charge = charge
                dbroom.status = status
                db.session.commit()
                msg = "Room Info Updated Successfully..!"
            else:
                dbroom = Room(id=rid,type=type,charge=charge,status=status)
                db.session.add(dbroom)
                db.session.commit()
                msg = "Room Info Created Successfully...!"

        return render_template('rooms.html',
                               resp = msg,user=session['userinfo'],
                               room = Room.dummy_room(),
                               roomlist = Room.query.all())
    return render_template('login.html', resp='')

@app.route('/rooms/edit/<int:rid>')
def edit_Room_info(rid):
    if 'userinfo' in session:
        return render_template('rooms.html',
                               resp='',user=session['userinfo'],
                               room=Room.query.filter_by(id=rid).first(),
                               roomlist=Room.query.all())
    return render_template('login.html', resp='')

@app.route('/rooms/delete/<int:rid>')
def delete_Room_info(rid):
    if 'userinfo' in session:
        msg = ''
        room = Room.query.filter_by(id=rid).first()
        if room:
            db.session.delete(room)
            db.session.commit()
            msg = "Room Removed Successfully..!"
        return render_template('rooms.html',user=session['userinfo'],
                               resp=msg,
                               room=Room.dummy_room(),
                               roomlist=Room.query.all())
    return render_template('login.html', resp='')

FLAG = True

@app.route('/rooms/<val>',methods=['GET'])
def toggle_room_type(val):
    if 'userinfo' in session:
        global FLAG
        allrooms = Room.query.all()
        if FLAG:
            if val == 'rid':
                allrooms.sort(key=lambda room : room.id,reverse =True)
            elif val == 'rtype':
                allrooms.sort(key=lambda room : room.type)
            elif val == 'rcharge':
                allrooms.sort(key=lambda room: room.charge)
            elif val == 'rstatus':
                allrooms.sort(key=lambda room: room.status)
            FLAG = False
        else:
            FLAG = True
        return render_template('rooms.html',user=session['userinfo'],
                               resp='',
                               room=allrooms,
                               roomlist=allrooms)
    return render_template('login.html', resp='')

if __name__ == '__main__':
    app.run(debug=True)