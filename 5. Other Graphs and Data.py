import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(170,5,250) #(mean,standard deviation, number of data points)
plt.hist(x)
plt.show()
