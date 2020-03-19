import sys
#fucntion to find the factorial
def fact(n):
	if n==0 or n==1:
		return 1
	return n*fact(n-1)

#function to find nCr = n! / ((n-r)! * r!)
def nCr(n,r):
	return fact(n)/(fact(n-r)*fact(r))

#This function will generate list of lists
def generate_pascal(n):
	a=[]
	#for each row
	for i in range(0,n+1):
		row=[]
		#find coefficients i.e. iCj
		for j in range(0,i+1):
			row.append(nCr(i,j))
		#append the row to list a
		a.append(row)
	#return the list a
	return a

#This function will print the pascal triangle
def print_triangle(coeffs):
	#for each row in list 
	for row in coeffs:
		#for each element in row
		for val in row:
			#print value in integer format
			print(int(val),end=" ")
		#print new line
		print()
#store argument in n
n = int(sys.argv[1])
#Call generate_pascal() with argument n
coeffs=generate_pascal(n)
#Call print_triangle() with argument coeffs
print_triangle(coeffs)

