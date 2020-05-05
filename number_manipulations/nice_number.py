def is_nice(n):
	temp = 0
	# Iterate till down number ends from last or n=0
	while n>0 and n%10>=temp:
		# Update temp
		temp = n%10
		n//=10
	# Iterate till up number ends or n=0
	while n>0 and n%10<=temp:
		# Update temp
		temp = n%10
		n//=10
	# If n is 0 then it is nice number, otherwise not nice number
	return n==0
# Function calling
print("123: ",is_nice(123))
print("2577: ",is_nice(2577))
print("598: ",is_nice(598))
print("321: ",is_nice(321))
print("775: ",is_nice(775))
print("123431: ",is_nice(123431))
print("4577852: ",is_nice(4577852))
print("123758: ",is_nice(123758))
print("4789089: ",is_nice(4789089))

