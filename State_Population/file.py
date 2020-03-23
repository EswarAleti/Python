def readData(fileName): 
	try:
		file = open(fileName,'r')
	#If file not found the prompt appropriate message
	except FileNotFoundError:
		print('Invalid file name try again...')
		#return empty lists
		return [],[]
	else:
		stateList=[]
		popList=[]
		#for each row of file
		for data in file:
			#split with respect to ,
			state,pop=data.split(',')
			#append data to lists
			stateList.append(state)
			popList.append(pop)
		#returns lists
		return stateList,popList

#Best case first state: AK
#Worst case last state: WY
def getPopLinear(stateList,popList,state):
	count=0
	#iterate over the list
	for i in range(0,len(stateList)):
		#increment count by 1
		count+=1
		#if state found return poplation
		if stateList[i]==state:
			print('\nLinear Search: comps = ',count)
			return popList[i]
	#If state not foun execution come here
	print('\nLinear Search: comps = ',count)
	print('Invalid state abbriviations')

#Best case state at 25th index: MS
#Worst case state at first or last: AK or WY
def getPopBinary(stateList,popList,state):
	low=0
	high=len(stateList)-1
	count=0
	while low<=high:
		#Increment count by 1
		count+=1
		#find mid
		mid = (low+high)//2
		#if state found the return population
		if stateList[mid]==state:
			print('\nBinary Search: comps = ',count)
			return popList[mid]
		elif stateList[mid]<state:
			low=mid+1
		else:
			high=mid-1
	##If state not foun execution come here
	print('\nBinary Search: comps = ',count)

def main():
	#iterate until valid file name given
	while True:
		fileName = input('Please the name of the data file: ')
		stateList,popList=readData(fileName)
		#if list size is greatar than 0 means valid file
		if len(stateList)>0:
			break
	state = input('Enter state abbrivation: ')
	population = getPopBinary(stateList,popList,state)
	getPopLinear(stateList,popList,state)
	#If state found
	if population is not None:
		print('The population of ',state,' is ',population)

if __name__=="__main__": 
    main() 