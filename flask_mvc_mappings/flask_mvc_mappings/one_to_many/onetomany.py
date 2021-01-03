from flask_mvc_mappings.flask_mvc_mappings.one_to_many.model import *
from flask import request,render_template

def get_avaiable_addresses():
    adrlist = Address.query.all()
    finaladr = []
    for adr in adrlist:
        if adr.studref:
            continue
        else:
            finaladr.append(adr)
    return finaladr

@app.route("/student/",methods=['GET','POST'])
def add_update_student():
    msg = ''
    if request.method == 'POST':
        formdata = request.form
        studId  = int(formdata['stid'])
        if studId:
            studrecord = Student.query.filter_by(id=studId).first()
            if studrecord:
                studrecord.fname = formdata.get('stfnm')
                studrecord.lname = formdata.get('stlnm')
                studrecord.fees = formdata.get('stfees')
                db.session.commit()
                msg = "Student ({}) Record Updated Successfully...!".format(studId)
        else:
            studadr = formdata.getlist('stadr')
            if studadr:
                adrlist = []
                for stadr in studadr:
                    adrrecord = Address.query.filter_by(id=stadr).first()
                    adrlist.append(adrrecord)

                stud = Student(fname=formdata.get('stfnm'),lname=formdata.get('stlnm'),fees=formdata.get('stfees'))
                stud.adrrefs.extend(adrlist) # 1 student will get many addresses
                db.session.add(stud)
                db.session.commit()
                msg = "Student ({}) Record Added Successfully...!".format(stud.id)
    return render_template('onetomany.html',
                           stud = Student.get_dummy_instance(),
                           studlist = Student.query.all(),
                           resp = msg,addresses = get_avaiable_addresses(),
                           flag = None)
@app.route("/student/<int:sid>",methods=['GET'])
def fetch_for_edit_student(sid):
    return render_template('onetomany.html',
                           stud=Student.query.filter_by(id=sid).first(),
                           studlist=Student.query.all(),addresses = get_avaiable_addresses(),
                           resp='',flag = None,students = Student.query.all())
@app.route("/student/<int:sid>",methods=['GET'])
def delete_student_record(sid):
    msg = ''
    studrecord = Student.query.filter_by(id=sid).first()
    if studrecord:
        db.session.delete(studrecord)
        db.session.commit()
        msg = "Student ({}) Record Deleted Successfully...!".format(sid)
    return render_template('onetomany.html',students = Student.query.all(),
                           stud=Student.get_dummy_instance(),
                           studlist=Student.query.all(),addresses = get_avaiable_addresses(),
                           resp=msg,flag = None)


@app.route("/address/",methods=['GET','POST'])
def add_update_address():
    msg = ''
    if request.method == 'POST':
        formdata = request.form
        adrId = int(formdata['adid'])
        if adrId:
            adrRecord = Address.query.filter_by(id=adrId).first()
            if adrRecord:
                adrRecord.city = formdata['adcity']
                adrRecord.state = formdata['adstate']
                adrRecord.pincode = formdata['adpin']
                db.session.commit()
                msg = "Address ({}) Record Updated Successfully...!".format(adrId)
        else:
            studid = int(formdata['student'])
            if studid:
                st = Student.query.filter_by(id=studid).first()
                adrrecord = Address(city=formdata['adcity'],state=formdata['adstate'],pin=formdata['adpin'])
                adrrecord.studref = st
                db.session.add(adrrecord)
                db.session.commit()
                msg = "Address ({}) Record Added Successfully...!".format(adrrecord.id)
    return render_template('onetomany.html',students = Student.query.all(),
                            address=Address.get_dummy_instance(),
                           adrlist=Address.query.all(),
                           resp=msg,flag = True)

@app.route("/address/<int:aid>",methods=['GET'])
def fetch_for_edit_address(aid):
    return render_template('onetomany.html',
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
    return render_template('onetomany.html',
                           address=Address.get_dummy_instance(),
                           adrlist=Address.query.all(),
                           resp=msg,flag = True)


if __name__ == '__main__':
    app.run(debug=True)