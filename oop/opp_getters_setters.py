class Human:
    def __init__(self, name: str, age: float):
        self.__name = name
        self.__age = age if age > 0 else 18


    def print_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age < 0:
            raise ValueError(f"Provided '{new_age = }' cannot be negative!")
        self.__age = new_age


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name



human_1 = Human("John", -5)
print(human_1.get_age())
human_1.set_age(50)
print(human_1.get_age())
print(human_1.name)
human_1.name = "Alex"
print(human_1.name)


# print(human_1._Human__age) # name mangling