def finalGrade(scoreList):
	hw1_weighted = float(scoreList[0])/10 * 0.05
	hw2_weighted = float(scoreList[1])/10 * 0.05
	mid_weighted = float(scoreList[2])/100 * 0.4
	fin_weighted = float(scoreList[3])/100 * 0.5
	final_grade = (hw1_weighted + hw2_weighted + mid_weighted + fin_weighted)*100
	return final_grade
#import csv module to read csv file
import csv
if __name__ == '__main__':

	scores = []
	#open csv file in read mode
	file = open('scores.csv', 'r')
	#read the opened file using csv reader
	reader = csv.reader(file)
	#append each row to scores list
	for row in reader:
		scores.append(row)
	#close the file
	file.close()

	names=[]
	#Open names.txt file in read mode
	file = open('names.txt', 'r')
	#append each name to names list
	for name in file:
		names.append(name.strip())
	#close the file
	file.close()

	#for each student call finalGrade() and print the result
	for i in range(len(names)):
		print(names[i],' earned ',round(finalGrade(scores[i]),2),'\b%')