import random

numRolls = 0
thisRoll = 0
six = False

while six == False:
  thisRoll = random.randint(1, 6)
  numRolls = numRolls + 1
  print('You rolled a ' + str(thisRoll))
  if thisRoll == 6:six = True

print('Congrats. You rolled a six in ' + str(numRolls) + ' tries.')
