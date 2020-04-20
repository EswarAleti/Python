import collections
def main():
	# Dictionary that stores the counters of graelevels
	grade_level_dict = {'Freshman':0, 'Sophomore':0, 'Junior':0, 'Senior':0}
	# Initial score is 0
	total_score=0
	# Initial number of students are 0
	no_students=0
	while True:
		# Menu
		print('1) Enter a student')
		print('2) Quit: ',end='')
		# User Choice
		choice = input()
		# Quitting
		if choice=='2':
			break
		# User input
		elif choice=='1':
			# Iterate until user enters valid gradelevel
			while True:
				grade_level = input('Enter grade level: ')
				if grade_level in grade_level_dict.keys():
					break
				print('Grade level should be Freshman/Sophomore/Junior/Senior')
			# Increment grade_level_counter
			grade_level_dict[grade_level]+=1
			# Iterate until user enters valid score
			while True:
				score = float(input('Enter score: '))
				if score>=0 and score<=100:
					break
				print('Score should be in range [0,100], Please try again...!')
			# Add score to total
			total_score+=score
			# Increment total number of students by 1
			no_students+=1
		# If user enters invalid choice 
		else:
			print('Invalid choice...!')
	# Calculate and print the result-0
	print('Freshman percentage: ',grade_level_dict['Freshman']/no_students*100,'%')
	print('Sophomore percentage: ',grade_level_dict['Sophomore']/no_students*100,'%')
	print('Junior percentage: ',grade_level_dict['Junior']/no_students*100,'%')
	print('Senior percentage: ',grade_level_dict['Senior']/no_students*100,'%')
	print('Average score: ',total_score/no_students)
if __name__ == "__main__":
	main()