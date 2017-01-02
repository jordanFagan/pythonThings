while True:
  value = (str (raw_input("Do you want to convert to celsius or to farenheit? (C/F)")))
  if value.lower() == "f":
    break
  elif value.lower() == "c":
    break
  else:
    print("Please try again")

if value.lower() == "f":
   f = "f"
else:
   f = "c"

while (True):   
  try:
    if f == "f":
     numberOne = (float (raw_input("Enter a number in Celsius you want converted to Farenheit: ")))
     numberRound = round((numberOne * 9 / 5 + 32) , 2)
     print ("Your number in Farenheit is " + str(numberRound))
     break
    else:
     numberOne = (float (raw_input("Enter a number in Farenheit you want converted to Celsius: ")))
     numberRound = round(((numberOne - 32) * 5 / 9) , 2)
     print ("Your number in Celsius is " + str(numberRound) + " (rounded to 2 d.p.).")
     break
  except ValueError as e :
    print ("Uh, oh. Something doesn't seem right there. Try a number instead!")
