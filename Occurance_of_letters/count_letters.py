file_name = input('Enter file name: ')
try:
	file = open(file_name,'r')
except:
	print('File not exist!')
occur_dict = {}
for line in file:
	line = line.lower()
	for letter in line:
		if letter.isalpha():
			occur_dict[letter] = occur_dict.get(letter,0)+1
print('Letter count:')
for k,v in occur_dict.items():
	print(k,'\t',v)
max_occur = max(occur_dict.values())
min_occur = min(occur_dict.values())
print('Letter(s) with highest count - ',max_occur)
for k,v in occur_dict.items():
	if v==max_occur:
		print(k)
print('Letter(s) with lowest count - ',min_occur)
for k,v in occur_dict.items():
	if v==min_occur:
		print(k)