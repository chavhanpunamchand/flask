from AcademyREST_API.producer.models import Student
from AcademyREST_API.producer.config import app
from AcademyREST_API.producer.student_service import *
from flask import request
import json

STUDENT_URI = "/api/student/"

sservice = StudentServiceImpl()

@app.route(STUDENT_URI,methods=['POST']) #http://127.0.0.1:5000/api/student/  POST with body
def add_student():
    reqdata = request.get_json()
    try:
        stud = Student(fullname = reqdata.get("student_fullname"),
                      age = reqdata.get("student_age"),
                      email = reqdata.get("student_email"),
                      photo = reqdata.get("student_photo"))
        flag = sservice.add_entity(stud)
        if flag:
            return json.dumps({"SUCCESS" : "Student Added Successfully..."})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR": "Problem in student Add.."})


@app.route(STUDENT_URI+"<int:stdid>",methods=['DELETE'])
def delete_student(stdid):
    try:
        flag = sservice.remove_entity(stdid)
        if flag:
            return json.dumps({"SUCCESS" : "Student Removed Successfully..."})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR": "Problem in student delete.."})


@app.route(STUDENT_URI+"<int:pid>",methods=['PUT'])
def update_student(stdid):
    try:
        reqdata = request.get_json()
        stud = Student(fullname=reqdata.get("student_fullname"),
                       age=reqdata.get("student_age"),
                       email=reqdata.get("student_email"),
                       photo=reqdata.get("student_photo"))
        flag = sservice.update_entity(stdid,stud)
        if flag:
            return json.dumps({"SUCCESS": "Student Updated Successfully..."})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR": "Problem in Student Update.."})


def serialize_product(stud):
   return {
        "student_id": stud.id,
        "student_fullname" : stud.fullname,
        "student_age" : stud.age,
       "student_email": stud.email,
       "student_photo": stud.photo
     }


@app.route(STUDENT_URI+"<int:pid>",methods=['GET']) #http://localhost:5000/api/product/{} GET
def get_student_details(stdid):
    try:
        student = sservice.fetch_entity(stdid)
        if student:
            return json.dumps({"SUCCESS":serialize_product(student)})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR": "No student With Given Id..!"})


@app.route(STUDENT_URI,methods=['GET'])
def get_all_student_details():
    try:
        students = sservice.fetch_all_entities()
        stud_list = []
        if students:
            for studs in students:
                stud_list.append(serialize_product(studs))
            return json.dumps({"SUCCESS":stud_list})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR": "No Student--Empty Table.."})



@app.route(STUDENT_URI+"photo/",methods=['POST'])
def add_student_with_photo():
    reqdata = request.form  # text format wala      request.form['name']      request.form.getlist('name')
    file = request.files['student_photo']           #request.files['dp']     request.files.getlist('dp')
    print("File",file)
    print("other data",reqdata)

    name = reqdata.get("student_name")
    file.save(name+".png")

    try:
        stud = Student(fullname = reqdata.get("student_fullname"),
                      age = reqdata.get("student_age"),
                      email = reqdata.get("student_email"),
                      photo = name+".png")
        flag = sservice.add_entity(stud)
        if flag:
            return json.dumps({"SUCCESS" : "Student Added Successfully..."})
    except BaseException as b:
        print(b.args)
    return json.dumps({"ERROR": "Problem in student Add.."})

if __name__ == '__main__':
    app.run(debug=True)
