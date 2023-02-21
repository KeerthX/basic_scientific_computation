#In this section we will visualize graphs of Trignometric Functions

#Sample rate and frequency is given (10000Hz,100Hz)

import numpy as np
import matplotlib.pyplot as plt

fs = 10000 #Sample Rate
fm = 100 #Frequency
w = 2*np.pi*fm/fs
n = 100
time = np.arange(0,n,1)
a = np.sin(w*time)
plt.plot(time,a)
plt.show()


#Lets also try the stem plot of the same

plt.stem(time,a)
plt.show()

#Lets now use the linspace function instead of the arange function and plot a cosine graph

t = np.linspace(-2*np.pi,2*np.pi,200)
amp = np.cos(t)
plt.plot(t,amp)
plt.show()

#Lets also plot the tan graph in the same in two methods using sin and cos and without it

time = np.linspace(-2*np.pi,2*np.pi,200)
amp_1 = np.tan(time)
plt.plot(time,amp_1)
plt.show()

time = np.linspace(-2*np.pi,2*np.pi,200)
amp_2 = np.sin(time)/np.cos(time)
plt.plot(time,amp_2)
plt.show()

#Lets also look at hyperbolic functions 
time = np.arange(-10,10,0.01)

sin_hyp = np.sinh(time)
cos_hyp = np.cosh(time)

plt.plot(time,sin_hyp)
plt.show()
plt.plot(time,cos_hyp)
plt.show()
