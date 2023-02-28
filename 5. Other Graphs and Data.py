# import numpy as np
# import matplotlib.pyplot as plt

# x = np.random.normal(170,5,250) #(mean,standard deviation, number of data points)
# plt.hist(x)
# plt.show()


import numpy as np

# Define a rectangular matrix A
A = np.array([[1, 1, 1], [1, 1, 1]])

# Compute the SVD of A
U, s, VT = np.linalg.svd(A)
print(U)
print(s)
print(VT)
print("-------------------------")
# Reconstruct the original matrix
S = np.zeros_like(A)
print(S)
print("-------------------------")
S[:min(A.shape), :min(A.shape)] = np.diag(s)
print(S)
print("-------------------------")
A_reconstructed = U.dot(S.dot(VT))
print(A.shape)
# Print the results
print("-------------------------")
print("Original matrix A =\n", A)
print("Reconstructed matrix A_reconstructed =\n", A_reconstructed)

