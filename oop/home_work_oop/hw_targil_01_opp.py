class Person:

   def __init__(self,name:str):
       self.name=name

   def get_name(self):
       return self.name

class Employee(Person):

    def __init__(self,name:str,salary:float,role:str):
        super().__init__(name)
        self.__salary= salary
        self.__role= role

    def get_salary(self):
        return self.__salary

    def set_salary(self,new_salary:float):
        if new_salary < 0:
           raise ValueError(f" Provided '{new_salary = }' cannot be negative!")
        else:
           self.__salary=new_salary

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self,new_role:str):
       if new_role.strip() == "":
          raise ValueError(f"{new_role } cannot be empty")
       else:
           self.__role= new_role

employee_1=Employee("yossi",30000,"teacher")
print(f'employee name : {employee_1.get_name()}')
print(f' employee salary: {employee_1.get_salary()}')
print(f'new role{employee_1.role}')
employee_1.set_salary(20000)
employee_1.role='daycare'
print(f'new salary {employee_1.get_salary()}')
print(f'new role{employee_1.role}')
try:
    employee_1.set_salary(-90)
except ValueError as e:
    print(f"validation error:{e}")







