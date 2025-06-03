from oop.home_work_oop.class_work.person import Person

class Student(Person):

   def __init__(self, name,student_id:int):
       super().__init__(name)
       self.__student_id=student_id


   def display_student_id(self):
       return  f" student id{self.__student_id}"

   @property
   def name(self):
       return self._name

   @name.setter
   def name(self, new_name):
       self._name = new_name

person_1=Person("david")
print(person_1.get_name())
student_1=Student("yossi",234556678)
print(student_1.name,student_1.display_student_id)
student_1.name="Alon"
print(student_1.name)
