def get_validity(password):
	# If password have less than 10 character then it is invalid
	if len(password)<10:
		return False
	# Initalize 3 varibales to False
	exist_digit = False
	exist_alpha = False
	exist_symbol = False
	# For each letter in password
	for letter in password:
		# If alphabet exist then make exist_alpha to True
		if letter.isalpha():
			exist_alpha = True
		# If digit exist then make exist_digit to True
		elif letter.isdigit():
			exist_digit = True
		# If symbol exist then make exist_symbol to True
		elif letter in '?!*':
			exist_symbol = True
	# This return true if 3 properties satisfied, False otherwise
	return exist_alpha and exist_digit and exist_symbol
# Function calling
print('is abc012 valid: ', get_validity('abc012'))
print('is abcdefg valid: ', get_validity('abcdefg'))
print('is AbC111! valid: ', get_validity('AbC111!'))
print('is AbC111def! valid: ', get_validity('AbC111def!'))