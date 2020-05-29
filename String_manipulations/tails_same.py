def tails_same(number_list):
	# First numebr of list
	first = number_list[0]
	# Last number of list
	last = number_list[len(number_list)-1]
	# It'll return true if first and last are equal, false otherwise
	return first==last
print(tails_same([1, 239, 949, 0, 84, 0, 1]))
print(tails_same([1, 239, 949, 0, 84, 0, 13]))

