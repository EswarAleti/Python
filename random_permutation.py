import random
A=[]
N=10
for i in range(0,N+1):
	A.append(i)
for i in range(2,N+1):
	Ran = random.randint(1,i)
	A[i],A[Ran]=A[Ran],A[i]
print(A)