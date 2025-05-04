removed_grades = []
grades = [80, 100, 95, 80, 105]
print(f"{grades = }")
print(id(grades))

removed_grades.append(grades.pop())
print(f"{grades = }")
print(id(grades))

removed_grades.append(grades.pop(1))
print(f"{grades = }")
print(id(grades))

print(f"{removed_grades = }")