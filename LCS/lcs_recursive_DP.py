import time

def lcs_recursive(i,j,X,Y):
	#If one of X,Y completed
	if i==-1 or j==-1:
		return 0
	#If there is a match
	if X[i]==Y[j]:
		return lcs_recursive(i-1,j-1,X,Y)+1
	#If there is no match
	return max(lcs_recursive(i-1,j,X,Y), lcs_recursive(i,j-1,X,Y))

def lcs_DP(X,Y):
	m = len(X)
	n = len(Y)
	#Initializing all entries of L table to 0
	L = [[0 for i in range(n+1)] for i in range(m+1)]  
	for i in range(1, m+1):
		for j in range(1, n+1):
			#If there is a match
			if X[i-1]==Y[j-1]:
				L[i][j] = L[i-1][j-1]+1
			#If there is no match
			else:
				L[i][j] = max(L[i-1][j], L[i][j-1])
	#return val
	return L[m][n]

#read file
file = open('rand1000000.txt','r')
#stroes all 6 digit nubers
arr = []
for line in file:
	for number in line.split():
		#If number is of 6 digits
		if len(number)==6:
			arr.append(number)

total_time_lcs_recursive = 0
for num in arr:
	start_time = time.time()
	#function call
	lcs_recursive(len(number)-1,9,number,'0123456789')
	end_time = time.time()
	#Add time to total for each call
	total_time_lcs_recursive += (end_time-start_time)
print('Total time that LCS recusive function take: ',total_time_lcs_recursive)

total_time_lcs_DP = 0
for num in arr:
	start_time = time.time()
	#Function call
	lcs_DP(number,'0123456789')
	end_time = time.time()
	#Add time to total for each call
	total_time_lcs_DP += (end_time-start_time)
print('Total time that LCS DP function take: ',total_time_lcs_DP)