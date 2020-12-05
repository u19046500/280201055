a = int(input("Enter the a:"))
b = int(input("Enter the b:"))
c = int(input("Enter the c:"))
disc = (b**2)-4*a*c

Real_1 = (-b+(disc**0.5))/(2*a)
Real_2 = (-b-(disc**0.5))/(2*a)

if disc > 0:
  print("There are two real roots:")
  print(Real_1)
  print(Real_2)
elif disc == 0:
  print("There is one real root")
  print(Real_1)
else:
  print("There are two complex roots")

