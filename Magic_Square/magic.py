class magic:
	#magic_square function
	def magic_square(self,n):
		i = 1
		print('Odd order Magic Square: ')
		for row in range(n):
			for col in range(n):
				#It follows 2*i+1 order
				print(2*i+1,end='\t')
				i+=1
			#new line
			print()

		i = 1
		print('Doubly-even order Magic Square: ')
		for row in range(n):
			for col in range(n):
				#It follows 4*i order
				print(4*i,end='\t')
				i+=1
			print()

		i = 1
		print('Singly-even order Magic Square: ')
		for row in range(n):
			for col in range(n):
				#It follows 4*i+2 order
				print(4*i+2,end='\t')
				i+=1
			print()
#creation of object for magic clcass
ms = magic()
#function calling
ms.magic_square(5)





