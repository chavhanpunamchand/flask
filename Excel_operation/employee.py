
'''This is emp strucutre to hold what is emp--> dev--defined employee type..'''
class Employee:
    def __init__(self,eid,enm,eag,esal,erol):
        self.empId  = int(eid)
        self.empName = enm
        self.empAge = int(eag)
        self.empSalary = float(esal)
        self.empRole = erol

    def __str__(self):
        return f'''\nEmp Id : {self.empId},Emp Name : {self.empName},Emp Age : {self.empAge},Emp Salary : {self.empSalary},Emp Role : {self.empRole}'''

    def __repr__(self):
        return str(self)

