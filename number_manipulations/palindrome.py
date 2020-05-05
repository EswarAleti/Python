def is_palindrome(n):
	# Initialization of variables
	temp = n
	pal = 0
	while temp>0:
		pal = (pal*10)+(temp%10)
		# Reduce temp by dividing with 10
		temp//=10
	# Returns true if n is palindrome, false otherwise
	return pal==n
# Function callings
print('10101: ',is_palindrome(10101))
print('131: ',is_palindrome(131))
print('1331: ',is_palindrome(1331))
print('1225221: ',is_palindrome(1225221))
print('2: ',is_palindrome(2))
print('122: ',is_palindrome(122))
print('100: ',is_palindrome(100))
print('19 : ',is_palindrome(19))


