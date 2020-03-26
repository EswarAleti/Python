def crossword(table,word):
	#index of row
	i=0
	#for each row in table
	for row in table:
		flag=0
		#check existence of each letter of word
		for letter in word:
			#if letter found in row then remove it from row
			if letter in row:
				row.remove(letter)
			#if letter not found in row then set flag=1 and stop process
			else:
				flag=1
				break
		#if flag=0 means word can be formed by row then return i
		if flag==0:
			return i
		#increment row index by 1
		i+=1
	#we come here if word cannot be formed
	return False

print(crossword( [['t','b','c','a'],
				  ['d','a','r','r'],
				  ['a','f','r','c']], 'car'))

print(crossword( [['t','b','c','a'],
				  ['d','a','r','r'],
				  ['a','f','r','c']], 'bar'))

print(crossword( [['t','b','c','a'],
				  ['d','a','r','r'],
				  ['a','f','r','c']], 'dad'))

print(crossword( [['t','b','c','a'],
				  ['d','a','r','r'],
				  ['a','f','r','c']], 'cab'))