


def calculate_average(number):
    if len(numbers)==0:
        return 0
    total_sum=0
    count=0
    for num in numbers:
        total_sum+=num
        count+=1
    average=total_sum/count
    return average

numbers= [10,20,30,40,50]
average_num= calculate_average(numbers)
print(average_num)

