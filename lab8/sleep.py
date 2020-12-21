import time
def timer(t):
  if t == 0:
    print("alert")
  else:
    time.sleep(1)
    print(t)
    t = t - 1
    timer(t)
timer(5)
    
