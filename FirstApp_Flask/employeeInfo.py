

class Employee:
    def __init__(self,eid,ename,eage,egen,ecity,esalary,email,erole,eskil,ehobs):
        self.empid=eid
        self.empName=ename
        self.empAge=eage
        self.eGender=egen
        self.empCity=ecity
        self.empSalary=esalary
        self.empEmail=email
        self.empRole=erole
        self.empSkill=eskil
        self.emphobs=ehobs

    def __str__(self):
        return f" EmpId : {self.empid}  " \
               f" Name :{self.empName}      " \
               f" Age :{self.eGender}" \
               f" City :{self.empCity}" \
               f" Salary:{self.empSalary}" \
               f" Role:{self.empRole} " \
               f" Email:{self.empEmail}" \
               f" Skill:{self.empSkill}" \
               f" Hobies:{self.emphobs}            "

    def __repr__(self):
        return self

# if __name__ == '__main__':
    # s1=Employee(101,'Punamchand',27,'M','Pune',25000,'chavhanpunamchand@gmail.com','SSE','Python,Java','Cricket,Hocky')
    # print(s1)

