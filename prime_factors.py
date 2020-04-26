def is_prime(n):
	#count stores number of factors of n
	count=0
	for i in range(1,n+1):
		#If factor found increment count
		if n%i==0:
			count+=1
	#It will return true if number of factors of n is 2, False otherwise
	return count==2

def factorize(n):
	factors = []
	for i in range(2,n//2+1):
		#If i is factor of n append it to list
		if n%i==0:
			factors.append(i)
	#return list
	return factors

def find_prime_factors(n):
	prime_factors = []
	#Find all factors of n
	factors = factorize(n)
	#For each factor
	for factor in factors:
		#If factor is prime then apped
		if is_prime(factor):
			prime_factors.append(factor)
	#return list
	return prime_factors

def list_to_str(li):
	#If list is empty then return empty string
	if len(li)==0:
		return ''
	s = ''
	#For each number of list append it to string and add ,
	for num in li:
		s+=str(num)+','
	#Remove last ,
	return s[:len(s)-1]

while True:
	start_num = int(input("Enter start number: "))
	#If valid number entered then break the loop
	if start_num > 0:
			break
	print("start must be positive")
while True:
	end_num = int(input("Enter end_number:"))
	#If valid number entered then break the loop
	if end_num > start_num:
		break
	print("End must be greater than start")

print('Factors of all numbers between',start_num,' and ',end_num,':')
for i in range(start_num,end_num+1):
	if is_prime(i):
		print(i,' : Prime!')
		continue
	#Print output
	print(i,' :',list_to_str(factorize(i)),'; Prime factors: ',list_to_str(find_prime_factors(i)))