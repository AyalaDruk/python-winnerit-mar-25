from xml.etree.ElementPath import prepare_parent


class Person:

   def __init__(self,name:str):
       self._name=name

   def get_name(self):
       return f"Name from Person class: {self._name}"


