def patterns(string):
   #Initialize count to 0
   count=0
   #Traverse till index len(string)-2
   for i in range(0,len(string)-2):
       #If 1st and 3rd letters matched and 1st and 2nd letters doesn't matched
       if string[i]==string[i+2] and string[i]!=string[i+1]:
           #Increment the count
           count+=1
   #return the count
   return count
#Function calling
first = 'axab'
print(patterns(first))
second = 'cdcece'
print(patterns(second))