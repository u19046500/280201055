num1 = input("Enter the first integer:")
num2 = input("Enter the second integer:")

min_len = len(num1)
if len(num2) < len(num1):
  min_len = len(num2)

match = 0

for i in range(1,min_len+1):
  if num1[-i] == num2[-i]:
    match = match + 1
print(match)    