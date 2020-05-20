def filter_word(word):
	new_word = ''
	for letter in word:
		if letter.isalpha():
			new_word+=letter
	return new_word
try:
	file = open('poem.txt','r')
except FileNotFoundError:
		print('Invalid file name try again...')
line_no=0
for line in file:
	words = line.split()
	for i in range(len(words)-1):
		if ',' in words[i]:
			print('Line {0}: {1},{2}'.format(line_no,filter_word(words[i]),filter_word(words[i+1])))
	line_no+=1