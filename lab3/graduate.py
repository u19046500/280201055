GPA = float(input("Enter the GPA:"))
Num_of_Lectures = float(input("Enter the number of lectures:"))
if GPA < 2:
  if Num_of_Lectures < 47:
    print("Not enough number of lectures and GPA!")
  else:
    print("Not enough GPA!")
else:
  if Num_of_Lectures < 47:
    print("Not enough number of lectures!")
  else:
    print("Graduated!!!")