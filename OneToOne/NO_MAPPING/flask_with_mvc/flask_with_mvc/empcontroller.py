from OneToOne.NO_MAPPING.flask_with_mvc.flask_with_mvc.config import app,db,example
from flask import request,render_template
from OneToOne.NO_MAPPING.flask_with_mvc.flask_with_mvc.models import Employee


@app.route("/emp/save/",methods=['POST',"GET"])
def add_or_update_emp():        #add/update
    msg = ""
    if request.method=='POST':
        formdata = request.form        # as its a post method
        eid = int(formdata.get('empid'))
        emp = Employee.query.filter_by(id=eid).first()
        if emp:
            emp.name = formdata.get('empname')
            emp.role = formdata.get('emprole')
            emp.salary = formdata.get('empsalary')
            db.session.commit()
            msg = "Emp Record Updated..!"
        else:
            #server will add adrid -->
            emp = Employee(name=formdata.get('empname'),role=formdata.get('emprole'),
                           salary=formdata.get('empsal'))
            db.session.add(emp)
            db.session.commit()
            msg = "Emp Record Saved into Database"
    return render_template('emp.html',
                           mapping = example,
                           emp = Employee.get_dummy_emp(),
                           emplist = Employee.query.all(),
                           resp = msg)

@app.route("/emp/edit/<int:eid>")   #pathvariable
def fetch_emp_for_edit(eid):    #fetch
    return render_template('emp.html',
                           mapping=example,
                           emp=Employee.query.filter_by(id=eid).first(),
                           emplist=Employee.query.all(),
                           resp='')


@app.route("/emp/delete/<int:eid>")   #pathvariable
def delete_address_record(eid): #delete
    msg = ''
    emp = Employee.query.filter_by(id=eid).first()
    if emp:
        db.session.delete(emp)
        db.session.commit()
        msg = "Employee Record Deleted "
    return render_template('emp.html',
                           mapping=example,
                           emp=Employee.get_dummy_emp(),
                           emplist=Employee.query.all(),
                           resp=msg)


if __name__ == '__main__':
    app.run(debug=True)