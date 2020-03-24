sentance = input()
words = sentance.split()
newSentance=''
for word in words:
	if word[:2] not in ['in','on','at','by'] and word[2:] not in ['.','?','!']:
		newSentance += word+' '
print(newSentance)