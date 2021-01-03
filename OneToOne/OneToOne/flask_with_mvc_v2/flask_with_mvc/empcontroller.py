from flask_with_mvc.config import app,db,example
from flask import request,render_template
from flask_with_mvc.models import Employee,Address


def only_not_selected_addresses():
    alladrs = Address.query.all()
    not_selected_adrs = []
    for adr in alladrs:
        if adr.empref==None:
            not_selected_adrs.append(adr)
    return not_selected_adrs

@app.route("/emp/save/",methods=['POST',"GET"])
def add_or_update_emp():        #add/update
    msg = ""
    if request.method=='POST':
        formdata = request.form        # as its a post method
        eid = int(formdata.get('empid'))
        emp = Employee(name=formdata.get('empname'), role=formdata.get('emprole'),
                       salary=formdata.get('empsal'))

        dbemp = Employee.query.filter_by(id=eid).first()
        if dbemp:
            dbemp.name = formdata.get('empname')
            dbemp.role = formdata.get('emprole')
            dbemp.salary = formdata.get('empsalary')
            db.session.commit()
            msg = "Emp Record Updated..!"
        else:
            #server will add adrid -->
            userselectedadr = int(formdata.get('address'))  # 0 or anyfk from address
            if float(formdata.get('empsal'))<0:
                msg = "Invalid salary"
            elif userselectedadr:  # address selected
                userselectedadr = Address.query.filter_by(id=userselectedadr).first() # aid vrn fetch entire address object from db
                emp.adrref = userselectedadr  # means to address -- emp la dya
                db.session.add(emp)  # emp with fk --
                db.session.commit()
                msg = "Emp Record Saved into Database"
                return render_template('emp.html',
                                       mapping=example,
                                       emp=Employee.get_dummy_emp(),
                                       emplist=Employee.query.all(),
                                       resp=msg,
                                       adrlist=only_not_selected_addresses())
            else:
                msg = "Address Not Selected"
            emp.id=0
            return render_template('emp.html',
                                   mapping=example,
                                   emp=emp,
                                   emplist=Employee.query.all(),
                                   resp=msg,
                                   adrlist=only_not_selected_addresses())

    return render_template('emp.html',
                           mapping = example,
                           emp = Employee.get_dummy_emp(),
                           emplist = Employee.query.all(),
                           resp = msg,
                           adrlist = only_not_selected_addresses())

@app.route("/emp/edit/<int:eid>")   #pathvariable
def fetch_emp_for_edit(eid):    #fetch
    return render_template('emp.html',
                           mapping=example,
                           emp=Employee.query.filter_by(id=eid).first(),
                           emplist=Employee.query.all(),
                           resp='',
                           adrlist = only_not_selected_addresses())



@app.route("/emp/delete/<int:eid>")   #pathvariable
def delete_emp_record(eid): #delete
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
                           resp=msg,
                           adrlist = Address.query.all())


if __name__ == '__main__':
    app.run(debug=True)