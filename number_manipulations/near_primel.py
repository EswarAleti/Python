def is_near_prime(n):
	# Initializing number of factors to 0
	no_of_factors = 0
	for i in range(1,n+1):
		# If n is divisible by i
		if n%i==0:
			# Increment number of factors by 1
			no_of_factors+=1
	# Returns true if n has atmost 4 factors, false otherwise
	return no_of_factors<=4
# Function calling
print('49: ',is_near_prime(49))
print('22: ',is_near_prime(22))
print('4: ',is_near_prime(4))
print('60: ',is_near_prime(60))
print('17: ',is_near_prime(17))
print('20: ',is_near_prime(20))


