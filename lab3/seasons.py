month = input("Enter the month:")
day = input("Enter the day of the month:")
if month in ["January", "February"]:
  print("It's winter!")
elif month in ["April", "May"]:
  print("It's Spring!")
elif month in ["July", "August"]:
  print("It's Summer!")
elif month in ["October", "November"]:
  print("It's Fall!")

if month == "March":
  if day < 20:
    print("It's winter!")
  else:
    print("It's Spring!")
if month == "June":
  if day < 21:
    print("It's Spring!")
  else:
    print("It's Summer!")
if month == "September":
  if day < 22:
    print("It's Summer!")
  else:
    print("It's Fall!")
if month == "December":
  if day < 21:
    print("It's Fall!")
  else:
    print("It's winter!")        