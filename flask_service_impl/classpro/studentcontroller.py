from flask_service_impl.classpro.models import db,app,Student,Address
from flask import request

STUD_MANDATORY_FIELDS  = ['stud_name', 'stud_email', 'stud_mobile']

def check_for_fields(rinfo,val = True):#{""}   --> 3 KEYS EXPECT KRTOY -> NAME,EMAIL,MOBILE
    errors = {}
    name = rinfo.get('stud_name')
    email = rinfo.get('stud_email')
    mobile = rinfo.get('stud_mobile')

    if not name:
        errors['stud_name'] = "Name field required"

    if not email:
        errors['stud_email'] = "email field required"
    else:
        stud = Student.query.filter(Student.email == email).first()
        if stud:
            errors['stud_email'] = "already given to {},{}".format(stud.id,stud.name)

    if not mobile and val:
        errors['stud_mobile'] = "mobile field required"

    return errors

import json
import smtplib
#open api -->
@app.route("/student/",methods=["POST"]) #http://localhost:5000/student     POST --> body -- {"stud_name":}
def add_new_student():
    rinfo= request.get_json()     # another applicaiton          # request.form --> browser thru
    if rinfo:
        errors = check_for_fields(rinfo)#
        if not errors:
            st = Student(name=rinfo.get('stud_name'),email=rinfo.get('stud_email'),mobile=rinfo.get('stud_mobile'))
            if rinfo.get('address'):
                adrid = int(rinfo.get('address'))
                dbadr = Address.query.filter_by(id=adrid).first()
                if dbadr:
                    st.address = dbadr
            db.session.add(st)
            db.session.commit()
            # write a code for --> send email -->
            return json.dumps({"success" :"Student Registered successfully.." })
        else:
            return json.dumps({"error" : errors})
    return json.dumps({"error": '{} required'.format(STUD_MANDATORY_FIELDS)})

@app.route("/student/<int:sid>",methods=["PUT"])
def update_student_info(sid):
    stud = Student.query.filter_by(id=sid).first()
    if stud:
        rinfo = request.get_json()
        errors = check_for_fields(rinfo,False)  #
        if not errors:
            stud.name = rinfo.get("stud_name")
            stud.email = rinfo.get("stud_email")
            stud.mobile = rinfo.get("stud_mobile")
            db.session.commit()
            return json.dumps({"success" : "Student Record Updated.."})
        return json.dumps({"error":errors})
    return json.dumps({"error":"No record with given id..!"})
@app.route("/student/<int:sid>",methods=["POST"])
def delete_student_info(sid):
    stud = Student.query.filter_by(id=sid).first()
    if stud:
        db.session.delete(stud)
        db.session.commit()
        return json.dumps({"success" : "Student record removed..!"})
    return json.dumps({"error" : "No student with given id so cannot remove..!"})

@app.route("/student/<int:sid>",methods=["GET"])
def get_student_info(sid):
    stud = Student.query.filter_by(id=sid).first() # database query fire -->
   # print(stud.__dict__)
    if stud:    # if student present inside database
        #stud.__dict__.pop('_sa_instance_state') # we are removing extra fields - nonserializable --
        return json.dumps({"success" : {"id":stud.id,"name": stud.name,"email":stud.email,"contact":stud.mobile}})
    return json.dumps({"error" : "No student given Id {} ".format(sid)})

@app.route("/student/",methods=["GET"])
def get_all_student_info():
    studs = Student.query.all()
    if studs:
        students = []
        for stud in studs:
            students.append({"id": stud.id, "name": stud.name, "email": stud.email, "mobile": stud.mobile})
        return json.dumps({"success" : students})
    return json.dumps({"error": "No Students"})

from flask_service_impl.classpro.models import StudBatchInfo,Batch

from datetime import datetime
def date_serialization(startdate):
    return "{}/{}/{} ,[DD/MM/YYYY]".format(startdate.day,startdate.month,startdate.year)

@app.route("/student/batch/<sid>",methods=["GET"])
def get_student_batch_details(sid):
    stud = Student.query.filter_by(id=sid).first() # check for student present or absent
    if stud:
        records = StudBatchInfo.query.filter(StudBatchInfo.studid==sid).all() # all records from that table -->
        all_batches  = []
        for record in records:
            batch = Batch.query.filter_by(batchcode=record.batchcode).first()
            all_batches.append({"BatchNo" : batch.batchcode,
                                "start": date_serialization(batch.startdate),
                                "end": date_serialization(batch.enddate),
                                "size" : batch.upperlimit,
                                "fees": record.fees})
        return json.dumps({"success" : all_batches})
    return json.dumps({"error" : "No Data with Given Id {}".format(sid)})


# this is the service for --> student operations -->
        #  single     all    remove
       #    get       get   delete   put*      post*
# course    get     getall  delete  update   add
# batch     get     getall  delete  update   add
# address   get     getall  delete  update   add
# client    get     getall  delete  update   add
#
if __name__ == '__main__':
    app.run(debug=True)
