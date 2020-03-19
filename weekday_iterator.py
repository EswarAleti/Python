def weekday_iterator(upto_day):
	
	days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
	# start iterating through the days
	for i in days:
		# check if we reached the upto_day to stop
		if i == upto_day:
			break
		# return the day for each iteration	
		yield i

# take input from the user
uptoDay = input("")

fh = open("file","w")

# iterate through the days using the function
for day in weekday_iterator(uptoDay):
	# for each iteration, write the day to a file
	fh.write(day+"\n")
fh.close

fh = open("file","r")
for day in fh:
	print(day,end="")
fh.close
# print Done! after finishing everything!
print("Done!")

