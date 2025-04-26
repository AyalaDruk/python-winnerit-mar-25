my_str1=input("enter a word:")
print(f'lowercase {my_str1.lower()}')
print(f'uppercase {my_str1.upper()}')
print(f'first  tab upper: {my_str1[0].upper()}{my_str1[1::].lower()}')
print(f'capitalized: {my_str1.capitalize()}')
print(f'title case: {my_str1.title()}')
words= my_str1.split()
print(f'words:{words}')



