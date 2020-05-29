def return_growing_num_list(max):
	num_list = []
	# Iterate from 1 to max(include)
	for i in range(1,max+1,1):
		# Initially num is empty
		num = ''
		# Iterate for i number of times
		for j in range(i):
			# Append i and tailing white space
			num += str(i)+' '
		# Append the num to list by removing last white space
		num_list.append(num[:len(num)-1])
	# Return the num_list
	return num_list
# Function calling and output printing
print(return_growing_num_list(3))
print(return_growing_num_list(4))

