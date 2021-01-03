from Excel_operation.employee import Employee


def get_input_from_user(idwant=False):
    eid = 0
    if idwant:
        print('Enter Values for Add Operations')
        eid = int(input('Enter Emp Id : '))
    else:
        print('Enter Values for update Operations')
    name = input('Enter Emp Name : ')
    eage = int(input('Enter Emp Age : '))
    esal = float(input('Enter Emp Salary : '))
    role = input('Enter Emp Role : ')
    return Employee(eid, name, eage, esal, role)
