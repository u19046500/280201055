year = int(input("Entre the year:"))
if year % 100 == 0:
  if year % 400 == 0:
    print("It's a leap year!")
  else:
    print("It's not a leap year!")
else:
  if year % 4 == 0:
    print("It's a leap year!")
  
  
  

