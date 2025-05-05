# names = ["Michal", "Deborah", "Ayala", "Alex"]
#
# def greet(names_to_iterate: list[str]):
#     for name in names_to_iterate:
#         print(f"Hi {name}!!!!")
#
# greet(names)


# names = ["Michal", "Deborah", "Ayala", "Alex"]


def greet(*args):
    # print(args)
    # print(type(args))
    for name in args:
        print(f"Hi {name}!!!!")

greet("Michal", "Deborah", "Ayala", "Alex")