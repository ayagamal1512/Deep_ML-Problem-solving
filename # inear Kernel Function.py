# inear Kernel Function

# Write a Python function kernel_function that computes the linear kernel between two input vectors x1 and x2. The linear kernel is defined as the dot product (inner product) of two vectors.

# Example:
# Input:
# import numpy as np

# x1 = np.array([1, 2, 3])
# x2 = np.array([4, 5, 6])

# result = kernel_function(x1, x2)
# print(result)
# Output:
# 32

'''solution'''

import numpy as np

def kernel_function(x1, x2):
	# Your code here
	kernel = np.dot(x1, x2)

	return kernel 
