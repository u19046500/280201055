num1 = float(input("Enter the first number:"))
min_num = num1
num2 = float(input("Enter the second number:"))
if num2 < min_num:
  min_num = num2
num3 = float(input("Enter the third number:"))
if num3 < min_num:
  min_num = num3
print(min_num)