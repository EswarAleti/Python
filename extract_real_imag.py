import random

def Real(z):
   #list that stores real part of complex numbers
   real = []
   #for every number
   for num in z:
       #append real part of complex number
       real.append(num.real)
   #return list
   return real

def Imag(z):
   #list that stores imaginary part of complex numbers
   imag = []
   #for every number
   for num in z:
       #append imaginary part of complex number
       imag.append(num.imag)
   #return list
   return imag

#generate some random complex numbers
z = []
for i in range(10):
   a = random.randint(-10,10)
   b = random.randint(-10,10)
   c = complex(a,b)
   z.append(c)

#function calling and output printing
print('complex numbers: ',z)
real = Real(z)
print('real part: ',real)
imag = Imag(z)
print('imaginary part: ',imag)