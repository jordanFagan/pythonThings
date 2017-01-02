while (True):
  railcard = (str (raw_input("Do you have a Railcard? (Y/N)")))
  if railcard.lower() == "y":
    break
  elif railcard.lower() == "n":
    break
  else:
    print("Please try again")

while (True):
  try:
    adultNo = float(raw_input("How many adults are traveling in your group? "))
    check = adultNo
    checkInt = int(check)
    if check == checkInt:
      break
    else:
      print ("Please enter a valid number")
  except ValueError:
      print ("That's not a number!")

while (True):
  try:
      adultPrice = float(raw_input("How much does one adult ticket cost? " + unichr(163)))
      break
  except ValueError:
      print ("Please enter a valid price.")

while (True):
  try:
    childNo = float(raw_input("How many children will be traveling with you?"))
    check1 = childNo
    check1Int = int(check1)
    if check1 == check1Int:
      break
    else:
      print ("Please enter a valid number")
  except ValueError:
      print ("That's not a number!")

while (True):
  try:
      childPrice = float(raw_input("And how much does one child ticket cost?" + unichr(163)))
      break
  except ValueError:
      print ("Please enter a valid price.")

if railcard.lower() == "y":
  priceTotal = float(((adultNo * adultPrice) + (childNo * childPrice)) / 100 * 80)
else:
  priceTotal = float(((adultNo * adultPrice) + (childNo * childPrice)))

print ("Your total price for your ticket(s) is " + unichr(163) + '%.2f' %priceTotal)
