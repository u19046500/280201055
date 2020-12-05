age = int(input("Enter your age:"))
if age < 6 or age > 60:
  print("You have %100 discount!")
  print("Bus ticket is free!")
elif age >= 6 and age <= 18:
  print("You have %50 discount!")
  print("Bus ticket price is 1.5TL!")
else:
  print("You have no discount!")
  print("Bus ticket price is 3TL!")

