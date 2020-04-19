def average(a_list):
	sum = 0
	for num in a_list:
		sum+=num
	return sum/len(a_list)

def standardDeviation(a_list):
	avg = average(a_list)
	square_diff = 0
	for num in a_list:
		square_diff += (avg-num)**2
	return (square_diff/len(a_list))**0.5

def median(a_list):
	a_list.sort()
	n = len(a_list)
	if n%2==0:
		return (a_list[n//2 - 1] + a_list[n//2])/2
	else:
		return a_list[n//2]

print('Average: ',average([5,3,1,2,4]))
print('Standard Deviation: ',standardDeviation([5,3,1,2,4]))
print('Median: ',median([5,3,1,2,4]))