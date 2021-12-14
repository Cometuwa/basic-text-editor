while 2 > 1:
  text = input("Write text: ")
  print("What do you want to do with it?")
  print("1 - make it uppercase")
  print("2 - capitalize first letter")
  print("3 - make it small")
  print("4 - split words")
  print("5 - check length")
  operation = input()
  if operation == "1":
    print(text.upper())
  elif operation == "2":
    print(text.capitalize())
  elif operation == "3":
    print(text.lower())
  elif operation == "4":
    print(text.split(" "))
  elif operation == "5":
    print(len(text))
  else:
    print("error")