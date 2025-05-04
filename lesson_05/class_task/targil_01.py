f_word=input("enter a first word:")
s_word=input("enter a second word:")
if f_word.lower()==s_word[::-1].lower():
    print("yes")
else:
    print("no")