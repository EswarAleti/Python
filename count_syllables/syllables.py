#This function returns true if word contains vowel, False otherwise
def is_syllable(word):
	#Converting word to uppercase
	word=word.upper()
	#If word contains vowel return True
	if 'A' in word or 'E' in word or 'I' in word or 'O' in word or 'U' in word :
		return True
	#exectioin comes here If word doesn't contains vowel
	return False

def get_num_syllables(poem_pronunciation):
	#syllables is a list that contains number of syllables
	syllables=[]
	for poem in poem_pronunciation:
		#Initial syllable count to 0
		count=0
		for line in poem:
			for word in line:
				#If word is syllable then increment the count
				if is_syllable(word):
					count+=1
		#Append count to syllables
		syllables.append(count)
	#Return syllables
	return syllables

#Function calling
print(get_num_syllables([[['L','IH1','T','AH0','L'],['JH','AE1','K'],['HH','A01','R','N','ER0']],[['S','AE1','T'],['IH0','N'],['AH0'],['K','A01','R','N','ER0']]]))
print(get_num_syllables([[['IH0','N']],[['M','EW1']],[['S' ,'IH0' ,'N']],[['H','EW1']],[['Y','UW1']]]))