password = "abc123"
inp_pw = input("enter the password:")
if inp_pw == 'help':
  print("first character is:", password[0])
elif password != inp_pw:
  print("wrong!")
else:
  print("welcome") and exit()

