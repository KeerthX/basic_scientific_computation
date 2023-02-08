#Matrices are an important part of Scientific Computation, they are used to plot graphs, simplify computation of linear equations and much more 
# In this section we will study about Matrices using the numpy package

import numpy as np 

#Ways to create an array 
a = np.array([[1,2,3],[4,5,6],[7,8,9]]) #This makes a 3x3 matrix with each [] representing a row
b = np.array([[1,1,1],[1,1,1],[1,1,1]]) #This makes a 3x3 matrix with each [] representing a row

#Addition of Matrices
c = a + b 
print(c) # c automatically becomes a matrix 

#Subtraction of Matrices
c = a - b 
print(c) # c automatically becomes a matrix 

#Multiply of Matrices
c = np.dot(a,b)
d = a @ b # Using the "@" operation 
print(c) # c automatically becomes a matrix 
print(d) # d automatically becomes a matrix 