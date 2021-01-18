list_ = [12, 56, 65, 6521, 21]
high = len(list_)-1
low = 0
x = 56

def binary(list_, x, low, high):
  while high >= low:

    mid = (low + high) // 2

    if list_[mid] == x:
      return mid
    elif list_[mid] < x:
      return binary(list_, x, mid+1, high)
    else:
      return binary(list_, x, low, mid-1)

  return -1

print(binary(list_, x, low, high))