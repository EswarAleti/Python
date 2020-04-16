#Open file in read mode
file = open('PresStates.txt','r')
states_list = []
#For each state in file
for state in file:
	#If state not exist in states_list then append state to list
	if state.strip() not in states_list:
		states_list.append(state.strip())
#Print number of states after deleting duplicates 
print(len(states_list))
#close the file
file.close()

#Open file in read meow
file = open('output.txt','w')
#Write each state of list into file
for state in states_list:
	file.write(state+'\n')
#close file
file.close()