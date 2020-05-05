def is_palindrome(n):
	temp = n
	pal = 0
	while temp>0:
		pal = (pal*10)+(temp%10)
		temp//=10
	return pal==n

def is_near_prime(n):
	no_of_factors = 0
	for i in range(1,n+1):
		if n%i==0:
			no_of_factors+=1
	return no_of_factors<=4

def is_nice(n):
	temp = 0
	while n>0 and n%10>=temp:
		temp = n%10
		n//=10
	while n>0 and n%10<=temp:
		temp = n%10
		n//=10
	return n==0

def update_scores(scores):
	# This score stores updated scores
	updated_scores = []
	# For each score in scores
	for score in scores:
		temp = score
		# If score is palindrome then double the score
		if is_palindrome(score):
			temp*=2
		# If score is near prime then double the score
		if is_near_prime(score):
			temp*=2
		# If score is nice then triple the score
		if is_nice(score):
			temp*=3
		# Append the score and updated score to the list
		updated_scores.append(score)
		updated_scores.append(temp)
	# Return the list
	return updated_scores
#User input
scores = input('Enter scores: ').split()
# Convert all scores to integers
scores = [int(x) for x in scores]
scores.sort()
# Function calling
updated_scores = update_scores(scores)
for i in range(0,len(updated_scores),2):
	print('{0},{1}'.format(updated_scores[i],updated_scores[i+1]),end=' ')