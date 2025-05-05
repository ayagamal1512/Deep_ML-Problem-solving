# One-Hot Encoding of Nominal Values

# Write a Python function to perform one-hot encoding of nominal values. The function should take in a 1D numpy array x of integer values and an optional integer n_col representing the number of columns for the one-hot encoded array. If n_col is not provided, it should be automatically determined from the input array.

# Example:
# Input:
# x = np.array([0, 1, 2, 1, 0])
#     output = to_categorical(x)
#     print(output)
# Output:
# # [[1. 0. 0.]
#     #  [0. 1. 0.]
#     #  [0. 0. 1.]
#     #  [0. 1. 0.]
#     #  [1. 0. 0.]]


#Solution:

import numpy as np

def to_categorical(x, n_col=None):
	# Your code here
	num_classes = np.max(x)+1 
	one_hot = np.eye(num_classes)[x]
	
	return one_hot