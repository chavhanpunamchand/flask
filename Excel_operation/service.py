from abc import ABC,abstractmethod

#what features that u are going to provide--> how --> inside impl classes-- [CSV,JSON,TXT,EXCEl,DB]
class EmpService(ABC):

    @abstractmethod
    def add_employee(self,emp):
        pass

    @abstractmethod
    def get_employee(self,empid):
        pass

    @abstractmethod
    def get_all_employees(self):
        pass

    @abstractmethod
    def delete_employee(self,empid):
        pass

    @abstractmethod
    def update_employee(self,empid,values):
        pass

    @abstractmethod
    def emp_avg_salary(self):
        pass

    @abstractmethod
    def get_rolebased_avg_salary(self):
        pass

    @abstractmethod
    def get_employees_based_on_role(self,rolenm):
        pass