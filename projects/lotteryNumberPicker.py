import random

lotteryNumbers = set()

while len(lotteryNumbers) < 6:
	lotteryNumbers.add(random.randint(1, 59))

sortedNumbers = list(lotteryNumbers)

sortedNumbers.sort(key = int)

print sortedNumbers
