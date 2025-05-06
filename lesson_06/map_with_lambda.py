numbers = [60, 80, 90, 100, 50, 45, 78, 90, 95]

def square_numbers(x: int):
    return x + 5

final_result = list(map(lambda x: x + 5 , numbers))
print(final_result)

print(square_numbers(5)) # call to the function

# provide function as parameter
final_result_2 = list(map(square_numbers, numbers))
print(final_result_2)


def work_with_list(list_of_nums: list[int]):
    new_list = []
    for num in list_of_nums:
        new_list.append(num + 5)
    return new_list



print(work_with_list(numbers))