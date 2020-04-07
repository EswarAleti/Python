def patterns(string):
	#If string length less than 3 then pattern will not exist so return 0
	if len(string)<3:
		return 0
	#If string length>=3 and 1st and 3rd letters matched and 1st and 2nd letters doesn't matched
	if string[0]==string[2] and string[0]!=string[1]:
		#Add 1 and call pattern() with string without 1st letter
		return 1+patterns(string[1:])
	#If pattern not exit call pattern() with string witout 1st letter
	return patterns(string[1:])
#Function calling
first = 'axab'
print(patterns(first))
second = 'cdcece'
print(patterns(second))