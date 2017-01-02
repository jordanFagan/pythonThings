import random

numberOfTries = 0

def main(sPlayersNumbers):
	lotteryNumbers = set()
	
	while len(lotteryNumbers) < 6:
		lotteryNumbers.add(random.randint(1, 59))
	
	sortedNumbers = list(lotteryNumbers)
	
	sortedNumbers.sort(key = int)
	
	#print("The drawn numbers numbers are " + str(sortedNumbers))
	
	sameNumbers = 0
	sameNumbersWere = ""
	
	for i in range(6):
		if sPlayersNumbers[i] in sortedNumbers:
			sameNumbers += 1
			sameNumbersWere += ", " + str(sPlayersNumbers[i])
			
	
	#if sameNumbers == 0:
		#print("You matched no numbers :(")
	
	#elif sameNumbers == 1:
		#print("You matched one number.")
		#print("It was" + str(sameNumbersWere))
	
	#else:
		#print("You matched " + str(sameNumbers) + " numbers")
		#print("They were" + str(sameNumbersWere))
	
	returnArray = [sameNumbers, sortedNumbers]
	
	return returnArray
	
sameNumbers = 0
firstHits = set([1, 2, 3, 4, 5, 6])

playersNumbers = set()
	
while len(playersNumbers) < 6:
	playersNumbers.add(random.randint(1, 59))

sPlayersNumbers = list(playersNumbers)

sPlayersNumbers.sort(key = int)
	
print("Your lucky dip numbers are " + str(sPlayersNumbers))

while sameNumbers != 6:
	numberOfTries += 1
	if numberOfTries % 100000 == 0:
		print("Try " + str(numberOfTries))
		
	returnArray = main(sPlayersNumbers)
	sameNumbers = returnArray[0]
	drawnNumbers = returnArray[1]
	
	if sameNumbers in firstHits:
		firstHits.remove(sameNumbers)
		print("You matched " + str(sameNumbers) + " on draw number " + str(numberOfTries))
		print("The numbers drawn were, " + str(drawnNumbers))

print("Try " + str(numberOfTries))
