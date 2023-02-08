#In this project we will learn about some basic math functions that is used in python for Scientific Computing

import cmath
x = 1 #Any Number 
y = 2 #Any Number 
z = complex(x,y)  #Converts the variables into a complex form x+iy
print(z)
rel = z.real #Gives the real part of the complex number 
print(rel)
img = z.imag #Gives the imaginary part of the complex number
print(img)
absolute = abs(z) #Gives the absolute value of the complex numebr
print(absolute)

