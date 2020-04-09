import random

def rollDice():
	#Initial sum is 0
	eyesSum=0
	#Roll for 4 times and add eye to eyesSum
	for i in range(4):
		eyesSum+=random.randint(1,6)
	#If eyesSum less than 9 player get 10 dollors
	if eyesSum<9:
		return 10
	#Else player loose 1 dollor
	else:
		return -1

#Assume Initial investment is 0
investment = 1000
#Play game for 1000 times
for i in range(1000):
	#Add winning/loosing amount to investment
	investment += rollDice()
print(investment)