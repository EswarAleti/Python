# This function will reverse a number
def reverse_number(num):
	rev_num = 0
	# Iterate until num becomes 0
	while num!=0:
		# Reversing from end
		rev_num = rev_num*10 + num%10
		# Reduce num
		num = num//10
	# Return the reversed number
	return rev_num

def reverse_number_in_list(number_list):
	new_list = []
	# For each number in number_list
	for num in number_list:
		# Reverse the number and append output to new_list
		new_list.append(reverse_number(num))
	# Return new_list
	return new_list

# Function calling and printing output
print(reverse_number_in_list([13, 45, 690, 57]))

