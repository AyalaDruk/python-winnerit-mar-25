my_str=input("enter a message:")
print(f'first character:{my_str[0]}')
print(f'last character:{my_str[-1]}')
mid_char= int(len(my_str)/2)
print(f'last middle char:{my_str[mid_char]}')
print(f'even index character:{my_str[0::2]}')
print(f'odd index character:{my_str[1::2]}')
print(f'reverse message:{my_str[::-1]}')



