#In this section we will deal with the various graphs and how we will be able to use them.
#We will use the matplotlib.pyplot library

#Visualizing Arrays 

import numpy as np 
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5,6,7,8,9,0])
plt.plot(x)
plt.show()

#Now lets make it more clear by using some labelling functions

plt.xlabel("Index X")
plt.ylabel("Index Y")
plt.plot(x)
plt.show()

#Lets now plot this array as a stem plot

plt.stem(x)
plt.show()
