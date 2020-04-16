import random
#Generate random 4-letter DNA
def getRandomDNA():
	letters=['A','C','G','T']
	return ''.join(random.choice(letters) for i in range(4))
#complement of DNA
def complementDNA(dna):
	comp=''
	for letter in dna:
		if letter=='A':
			comp+='T'
		elif letter=='T':
			comp+='A'
		elif letter=='C':
			comp+='G'
		elif letter=='G':
			comp+='C'
	return comp
#generate a random DNA call it as original
original = getRandomDNA()
print(original)
count=0
while True:
	#Generate another random DNA
	randomDNA = getRandomDNA()
	#If above dna is equal  to complement of original DNA stop process
	if randomDNA==complementDNA(original):
		print(count)
		print(randomDNA)
		break
	#Increment count by 1cls
	count+=1



	