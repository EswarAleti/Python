class MyTime:
	#constructor
	def __init__(self,hr,min,sec):
		self.hr=hr
		self.min=min
		self.sec=sec

	def displayTime(self):
		return str(self.hr)+':'+str(self.min)+':'+str(self.sec)
	#method that finds intervel minutes bettween any two times
	def getMin(self,timeObj):
		res = 0

		#if self object has more time than passed object
		if self.hr>timeObj.hr:
			#find number of hours and each hour has 60 minutes
			res = abs(self.hr - timeObj.hr)*60
			#10:23 09:13 case
			if self.min<timeObj.min:
				res -= abs(self.min-timeObj.min)
			#10:23 09:33 case
			else:
				res += abs(self.min-timeObj.min)
		#if passed object has more time than self object	
		elif timeObj.hr>self.hr:
			#find number of hours and each hour has 60 minutes
			res = abs(self.hr - timeObj.hr)*60
			#9:13 10:23 case
			if timeObj.min<self.min:
				res -= abs(self.min-timeObj.min)
			#9:33 10:23 case
			else:
				res += abs(self.min-timeObj.min)
		#within the same hours
		else:
			res = abs(self.min-timeObj.min)
		return res
time1 = MyTime(10,23,49)
time2 = MyTime(9,13,49)
time3 = MyTime(9,33,49)
print('Intervel minutes between ',time1.displayTime(),' and ',time2.displayTime(),' is ',time1.getMin(time2),' minutes')
print('Intervel minutes between ',time1.displayTime(),' and ',time3.displayTime(),' is ',time1.getMin(time3),' minutes')
print('Intervel minutes between ',time2.displayTime(),' and ',time1.displayTime(),' is ',time2.getMin(time1),' minutes')
print('Intervel minutes between ',time3.displayTime(),' and ',time1.displayTime(),' is ',time3.getMin(time1),' minutes')