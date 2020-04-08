import os
from os import listdir
from os.path import isfile, join

def isFileOrPath(path):
	#If path is a directory
	if os.path.isdir(path):  
		displayFilesInDirectory(path)
	#If path is a file
	else:
		displayFile(path)

#This function will print content of file in given path
def displayFile(path):
	print('File name: ',path)
	#Open a file
	file = open(path,'r')
	for line in file:
		print(line.strip())
#This function will print content of each file in given path
def displayFilesInDirectory(path):
	#List all files in given directory
	directory = [f for f in listdir(path) if isfile(join(path, f))]
	#For each file in directory
	for file in directory:
		print('File name: ',path+"\\"+file,end=' ')
		#Open file
		file = open(path+"\\"+file,'r')
		#Print Content of the file
		for line in file:
			print(line.strip(),end = ' ')
		#Print newline after each file
		print()

#isFileOrPath("C:\\Users\\srini\\Desktop\\Input\\input1.txt")
isFileOrPath("C:\\Users\\srini\\Desktop\\Input")