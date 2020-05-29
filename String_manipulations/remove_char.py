def remove_char(str_list, str):
	new_list = []
	# For each word in str_list
	for word in str_list:
		# Replace the str in the word with empty string and append it to new_list
		new_list.append(word.replace(str,''))
	# Return new_list
	return new_list
# Function calling and output printing
print(remove_char(['adndj', 'adjdlaa', 'aa', 'djoe'],'a'))

