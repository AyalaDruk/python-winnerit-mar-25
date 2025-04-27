numbers=list(range(1,17))
num=numbers.pop(15)
#print the list numbers after remove the last num
print(f'numbers = {numbers}')
num+= numbers.pop(0)
num+=numbers.pop(12)
num+=numbers.pop(7)
print(f'sum of remove:{num}')





