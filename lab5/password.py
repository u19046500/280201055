password = "abc123"
word = input("Enter password: ")
if word == "help":
  print(password[0])
elif word == password:
  print("Welcome")
else:
  print("Wrong")