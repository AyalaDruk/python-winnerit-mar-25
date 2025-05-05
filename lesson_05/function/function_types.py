import datetime

# 1. No parameters and no return

# def say_hello():
#     print("Hello Everyone!")
#     print("Hello from here")
#
# say_hello()

# 2. Parameters and no return
# def say_hello_with_param(name: str, age: float):
#     print(f"Hello {name.upper()}! Next year you will be: {age + 1}")
#
#
# say_hello_with_param(name="Alex", age=37)

# def check_weather(city: str = "Jerusalem"):
#     print(f"Checking weather in {city}")
#     print(f"A weather is fine!")
#
# check_weather()
# check_weather("New York")

# 3 Return + Parameters

# def calculate_sum(first_num: int, second_num: int) -> int | str:
#     if first_num < 0 or second_num < 0:
#         return "Invalid input"
#     return first_num + second_num
#
# result = calculate_sum(10, 20)
# print(result)
# print(calculate_sum(50, 100))
# print(calculate_sum(-5, 100))

# Return, no params
# def get_current_time():
#     return datetime.datetime.now()
#
# print(get_current_time())