def remove_punctuations(word):
	#For each letter
	for letter in word:
		#If letter is a sepcial character then remove
		if not letter.isalnum():
			word=word.replace(letter,'')
	#return word
	return word

def print_top_five(count_of_words_dict):
	print('\nTop 5 frequent words are:')
	#Get top 5 keys as a list
	top_five_words = sorted(count_of_words_dict, key=count_of_words_dict.get, reverse=True)[:5]
	#For each word in top 5 words
	for word in top_five_words:
		#Print word and it's occurance in formatted way
		print(f'\t{word:11}: {count_of_words_dict[word]:5d}')

def print_top_ten(count_of_words_dict):
	print('\nTop 10 frequent words are:')
	#Get top 10 keys as a list
	top_ten_words = sorted(count_of_words_dict, key=count_of_words_dict.get, reverse=True)[:10]
	#For each word in top 10 words
	for word in top_ten_words:
		#Print word and it's occurance in formatted way
		print(f'\t{word:11}: {count_of_words_dict[word]:5d}')

#To store number of words
count_of_words = 0
#To store number of praragraphs
count_of_paragraph = 0
#To store words
words_list = []
#TO store words and its occurances
count_of_words_dict = {}
#Open file
with open('hw7_article.txt') as file:
	#For each line in file
	for line in file:
		#Increment number of paragraphs by 1
		count_of_paragraph+=1
		#For each word in line
		for word in line.split():
			#Increment number of words by 1
			count_of_words+=1
			#call remove_punctuation() by passing word as parameter
			word=remove_punctuations(word).lower()
			#append word to words_list
			words_list.append(word)
			#Add word to dectionary and increment it's occurance by 1 if exist, 0 otherwise
			count_of_words_dict[word] = count_of_words_dict.get(word,0)+1

#Output
print('Total number of paragraph is: ',count_of_paragraph)
print('Total number of words are: ',count_of_words)
print('\nFirst 5 words are:\n\t',words_list[:5])
print('\nLast 5 words are:\n\t',words_list[len(words_list)-5:])
print_top_five(count_of_words_dict)
print_top_ten(count_of_words_dict)