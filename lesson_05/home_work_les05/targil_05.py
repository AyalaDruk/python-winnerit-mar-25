



def max3(*args):
    if len(args)==0:
         return "No numbers were given"
    max_value= args[0]
    for num in args:
     if num>max_value:
         max_value=num

    return max_value






max_number=max3(3,7,9,8,6)
print(max_number)
empty_result= max3()
print(empty_result)
