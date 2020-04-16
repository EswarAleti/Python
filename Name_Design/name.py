import time
file = open("name.txt",'r')
for line in file:
	for letter in line:
		print(letter)#,end='')
		time.sleep(0.5)