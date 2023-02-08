#In this project we will learn about some basic math functions that is used in python for Scientific Computing

#Complex Functions

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

#Trignometric Functions

import numpy as np 

t = 0 #This is the angle in radians

x = np.sin(t) #This returns the sine value
print(x)
y = np.cos(t) #This returns the consine value
print(y)
z = np.tan(t) #This returns the tan value
print(z)