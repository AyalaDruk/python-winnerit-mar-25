class Person:

   def __init__(self,name:str):
       self._name=name

   def get_name(self):
       return self._name

   def set_name(self,new_name:str):
       self._name=new_name


