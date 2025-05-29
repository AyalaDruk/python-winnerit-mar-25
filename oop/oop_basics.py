class Person:
    def __init__(self, name: str = "default", age: float = 18, country: str = "Israel", job: int = 0):
        self.name = name
        self.age = age
        self.country = country
        self.job = job

    def say_hello(self):
        print(f"Hello, {self.name}!")

    def get_age(self):
        return self.age


# person = {
#     "name": "John",
#     "age": 36,
#     "country": "Israel"
# }
#
# person_2 = {
#     "name": "John",
#     "age": 36
# }

person_object = Person("Alex", 37.6, "Belarus", 5)
person_object.say_hello()
print(person_object.get_age())
print(person_object.job)

person_object_2 = Person("Israeli Israeli", 60, "Israel")
person_object_2.say_hello()
print(person_object_2.get_age())
print(person_object_2.job)

person_empty = Person(name="Name")
person_empty.say_hello()