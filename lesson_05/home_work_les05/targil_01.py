age = int(input("enter your age"))
has_ticket = input("you have a ticket ? yes/no")
if has_ticket =="yes":
    has_ticket=True
else:
    has_ticket = False
has_permission = input("you has_permission ? yes/no")
if has_permission =="yes":
    has_permission=True
else:
    has_permission = False

if age >= 18 and has_ticket == True:
    print("you can enter the club")
if age >= 18 and  has_ticket== False:
    print("you cant enter the club")
if age < 18 and has_permission == True:
    print("you can enter the club with the special permission")
if age < 18 and  has_permission == False:
    print("you cant enter the club with the special permission")
