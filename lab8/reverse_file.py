my_list = [1,2,3,4]
def reverse(l):
  if len(l) == 0:
    return []

  return [l.pop()] + reverse(l)

print(reverse(my_list))
    