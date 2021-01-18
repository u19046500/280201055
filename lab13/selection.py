
def select_sort(list_, n):
  min_ = list_[n]
  if n == len(list_)-1:
    return list_
  else:
    for i in list_[n+1:]:
      if i < min_:
        min_ = i

    list_[n], list_[min_] = list_[min_], list_[n]

    return select_sort(list_, n+1)

n = 0
list_ = [1,65,8452,7813,2]
new_list = select_sort(list_, n)
print(new_list)