number = int(input("Enter the number:"))
starting_number = number
power = int(input("Enter the power:"))
for i in range(power-1):
  starting_number = starting_number*number
print(starting_number)