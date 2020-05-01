# User input for N
N = int(input('Enter value of N: '))
print('List of numbers:')
# User input for number and store into burstList
burstList  = [int(x) for x in input().split()]

# Initialization of list and variables
BurstLengths = []
burst_open = 0
burst_length = 0
# For each number in burstList
for val in burstList:
	# If non zero number
	if val!=0:
		# If burst_length is non_zero then append it to BurstLengths
		if burst_length!=0:
			BurstLengths.append(burst_length)
		# Change state of variable
		burst_open = 0
		burst_length = 0
	# If value is zero
	elif val==0:
		# Change srtate of variable
		burst_open = 1
		# Increment burst_length by 1
		burst_length += 1
# If last val is 0 then burst_length will be non-zero
if burst_length!=0:
	BurstLengths.append(burst_length)

# Print output
print('Burst Length ')
index = 0
# Traverse BurstLengths using while loop
while index<len(BurstLengths):
	# Print length
	print(index+1,' ',BurstLengths[index])
	# Increment index by 1
	index+=1

# Find sum of lengths in BurstLengths
total=0
for val in BurstLengths:
	total+=val

# Print output
print('Average burst length: ',round(total/len(BurstLengths),2))
print('Minimum burst length: ', min(BurstLengths))
print('Maximum burst length: ', max(BurstLengths))
print('Total number of zeros: ', total)