# from flask_initial_web_service_demo.login_controller import *
from flask_initial_web_service_demo.model import *
from flask_initial_web_service_demo.config import *
from flask import request,render_template

@app.route("/rooms/",methods=['GET','POST'])
def add_update_rooms():
    msg = ''
    if request.method == 'POST':
        formdata = request.form
        roomId  = int(formdata['id'])
        if roomId:
            roomrecord = Hotel.query.filter_by(id=roomId).first()
            if roomrecord:
                roomrecord.charge = formdata.get('charge')
                roomrecord.type = formdata.get('type')
                roomrecord.status = formdata.get('status')
                db.session.commit()
                msg = "room ({}) Record Updated Successfully...!".format(roomId)
        else:
            room= Room(id=formdata.get('id'),type=formdata.get('type'),charge=formdata.get('charge'),status=formdata.get('status'),hotelid=formdata.get('hotel_id'))
            db.session.add(room)
            db.session.commit()
            msg = "room ({}) Record Added Successfully...!".format(room.id)
    TYPES = ['STANDARD', 'DELUX', 'NORMAL', 'PREMIUM']
    return render_template('rooms.html',
                           types=TYPES,
                           roomlist = Room.query.all(),
                           resp = msg)


'''

@app.route("/room/<int:sid>",methods=['GET'])
def fetch_for_edit_student(sid):
    return render_template('onetoone.html',
                           stud=Student.query.filter_by(id=sid).first(),
                           studlist=Student.query.all(),addresses = get_avaiable_addresses(),
                           resp='',flag = None)
@app.route("/student/<int:sid>",methods=['GET'])
def delete_student_record(sid):
    msg = ''
    studrecord = Student.query.filter_by(id=sid).first()
    if studrecord:
        db.session.delete(studrecord)
        db.session.commit()
        msg = "Student ({}) Record Deleted Successfully...!".format(sid)
    return render_template('onetoone.html',
                           stud=Student.get_dummy_instance(),
                           studlist=Student.query.all(),addresses = get_avaiable_addresses(),
                           resp=msg,flag = None)


@app.route("/address/<int:aid>",methods=['GET'])
def fetch_for_edit_address(aid):
    return render_template('onetoone.html',
                           address=Address.query.filter_by(id=aid).first(),
                           adrlist=Address.query.all(),
                           resp='',flag = True)
@app.route("/address/<int:aid>",methods=['GET'])
def delete_address_record(aid):
    address = Address.query.filter_by(id=aid).first()
    if address:
        db.session.delete(address)
        db.session.commit()
        msg = "Address ({}) Record Deleted Successfully...!".format(aid)
    return render_template('onetoone.html',
                           address=Address.get_dummy_instance(),
                           adrlist=Address.query.all(),
                           resp=msg,flag = True)

'''
if __name__ == '__main__':
    app.run(debug=True)