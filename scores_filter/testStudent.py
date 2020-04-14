from student import Student
import random

def main():
	student = Student("Ken", 5)
	print(student)
	#Randomlt set 5 scores
	for i in range(5):
		student.setScore(i,random.randint(0,100))
	print(student)

	#Get the score array
	scoreArr = student.getScoreArray()
	#Using filter & lambda functions, to get scores that greater than 60
	result = (list(filter(lambda x:x>60,scoreArr)))
	print(*result)
if __name__ == "__main__":
	main()