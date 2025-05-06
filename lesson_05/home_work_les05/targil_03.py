any_month=input("enter a month:")

match any_month.title().strip():
  case "December"|"January"|"February":
    print("Winter")
  case "March"|"April"|"May":
    print("Spring")
  case "June"| "July"| "August":
    print("Summer")
  case "September"| "October"| "November":
    print("Fall")
  case _:
    print("Invalid day")




