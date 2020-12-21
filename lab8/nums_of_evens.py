numList = [0, 1, 2, 3, 4, 5]
def evens(a):
  even = 0
  for i in a:
    if i % 2 == 0:
      even = even + 1
  return even

print(evens(numList))