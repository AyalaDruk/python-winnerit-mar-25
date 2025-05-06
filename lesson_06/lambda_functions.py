def calculate_result(x, y):
    result = x ** y
    return result

calculation = lambda x, y: x ** y
result_final = calculation(5, 3)
print(result_final)
print(calculate_result(5, 3))

print_with_lambda = lambda x: print(x)
print_with_lambda("Hello World")

# function name(params) {}
# const name = (params) => {}
# name()