N = int(input("How many Fibonacci numbers you need?"))
numList = []
num0, num = 0, 1
for i in range(1, N+1):
  numList.append(num)
  num, num0 = num + num0, num
print(numList)