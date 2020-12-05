N = int(input("How many numbers?"))
evens = 0
for i in range(N):
  n = int(input("Enter the integer:"))
  if n % 2 == 1:
    evens = evens + 1
print("% of evens =", (evens/N)*100)