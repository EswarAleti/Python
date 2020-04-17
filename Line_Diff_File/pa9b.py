#Opening file
try:
	file1 = open("file1.txt","r")
except:
	print("File1 not exist")
	exit()

try:
	file2 = open("file2.txt","r")
except:
	print("File2 not exist")
	exit()

#reading data in files into lists
lines_file1 = []
lines_file2 = []
for line in file1:
	lines_file1.append(line)
for line in file2:
	lines_file2.append(line)

i=0
#Iterate until one of list ends
while i<len(lines_file1) and i<len(lines_file2):
	print("File 1: ",lines_file1[i].strip())
	print("File 2: ",lines_file2[i].strip())
	print("Diff:    ",end='')
	j=0
	#Iterate until one line ends
	while j<len(lines_file1[i]) and j<len(lines_file2[i]):
		#If match then print white space
		if lines_file1[i][j]==lines_file2[i][j]:
			print(' ',end='')
		#If not match then print x
		else:
			print('x',end='')
		#Increment j by 1
		j+=1
	#For remaining letters of line print x
	while j<len(lines_file1[i]):
		print('x',end='')
		j+=1
	#For remaining letters of line print x
	while j<len(lines_file2[i]):
		print('x',end='')
		j+=1
	#Increment i by 1
	i+=1
	#new line
	print()
#For other lines just print x for each letter
while i<len(lines_file1):
	print("File 1: ",lines_file1[i].strip())
	print("File 2: ")
	print("Diff:    ",end='')
	for letter in lines_file1[i]:
		print('x',end='')
	i+=1

#For other lines just print x for each letter
while i<len(lines_file2):
	print("File 1: ")
	print("File 2: ",lines_file2[i].strip())
	print("Diff:    ",end='')
	for letter in lines_file2[i]:
		print('x',end='')
	i+=1